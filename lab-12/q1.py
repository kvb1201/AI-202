# 1. A tech hub has 6 different project teams (P1 to P6) that need to meet tomorrow.
# However, there are only 3 meeting rooms available (R1,R2,R3). Some teams
# have overlapping members and therefore cannot meet at the same time.
# Constraints (Incompatibility List):
# ● P1 conflicts with: P2,P3,P6
# ● P2 conflicts with: P1,P3,P4
# ● P3 conflicts with: P1,P2,P5
# ● P4 conflicts with: P2,P6
# ● P5 conflicts with: P3,P6
# ● P6 conflicts with: P1,P4,P5
# Task Requirements:
# Initial State: Set the domain for every project variable to {R1,R2,R3}.
# 1. Constraint Enforcement: Apply AC-3 to this constraint graph.
# 2. Step-by-Step Trace: Provide a trace of the first 5 arc-reductions (e.g., "Arc
# (P1,P2) checked, no change").
# 3. Consistency Check: After running AC-3, determine if the problem is
# arc-consistent.
# If we preemptively assign Team 1 to Room 1 , does AC-3 detect a failure, or does it
# leave a valid set of domains for the remaining rooms?

from collections import deque
import copy

variables = ['P1','P2','P3','P4','P5','P6']

domains_init = {
    'P1': ['R1','R2','R3'],
    'P2': ['R1','R2','R3'],
    'P3': ['R1','R2','R3'],
    'P4': ['R1','R2','R3'],
    'P5': ['R1','R2','R3'],
    'P6': ['R1','R2','R3'],
}

conflicts = {
    'P1':['P2','P3','P6'],
    'P2':['P1','P3','P4'],
    'P3':['P1','P2','P5'],
    'P4':['P2','P6'],
    'P5':['P3','P6'],
    'P6':['P1','P4','P5']
}


def revise(domains, Xi, Xj):
    revised = False
    to_remove = []

    for x in domains[Xi]:
        found = False
        for y in domains[Xj]:
            if x != y:
                found = True
                break
        
        if not found:
            to_remove.append(x)

    for x in to_remove:
        domains[Xi].remove(x)
        revised = True

    return revised


def AC_3(domains):
    queue = deque()

    # initialize all arcs
    for Xi in conflicts:
        for Xj in conflicts[Xi]:
            queue.append((Xi, Xj))

    steps = 0  

    while queue:
        Xi, Xj = queue.popleft()

        if steps < 5:
            before = domains[Xi].copy()

        changed = revise(domains, Xi, Xj)

        if steps < 5:
            if changed:
                print(f"Arc ({Xi},{Xj}) checked → domain reduced: {before} -> {domains[Xi]}")
            else:
                print(f"Arc ({Xi},{Xj}) checked → no change")
            steps += 1

        if changed:
            if len(domains[Xi]) == 0:
                return False

            for Xk in conflicts[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))

    return True


def solve():
    print("---- Case 1: Normal AC-3 ----")
    domains = copy.deepcopy(domains_init)

    result = AC_3(domains)

    print("\nFinal Domains:")
    for var in variables:
        print(var, ":", domains[var])

    print("\nArc Consistent:", result)


    print("\n---- Case 2: Assign P1 = R1 ----")
    domains = copy.deepcopy(domains_init)
    domains['P1'] = ['R1']

    result = AC_3(domains)

    print("\nFinal Domains:")
    for var in variables:
        print(var, ":", domains[var])

    print("\nFailure Detected:", not result)


solve()