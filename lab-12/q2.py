from collections import deque
import copy

# ---------------- INPUT ----------------
grid = [
[0,0,0,0,0,6,0,0,0],
[0,5,9,0,0,0,0,0,8],
[2,0,0,0,0,8,0,0,0],
[0,4,5,0,0,0,0,0,0],
[0,0,3,0,0,0,0,0,0],
[0,0,6,0,0,3,0,5,0],
[0,0,0,0,0,7,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,5,0,0,0,2]
]

# ---------------- VARIABLES ----------------
cells = [(r, c) for r in range(9) for c in range(9)]

# ---------------- DOMAINS ----------------
domains = {}

for r in range(9):
    for c in range(9):
        if grid[r][c] == 0:
            domains[(r,c)] = [1,2,3,4,5,6,7,8,9]
        else:
            domains[(r,c)] = [grid[r][c]]

# ---------------- NEIGHBORS ----------------
def get_neighbors(r, c):
    neighbors = set()

    # row + col
    for i in range(9):
        if i != c:
            neighbors.add((r, i))
        if i != r:
            neighbors.add((i, c))

    # box
    br = (r//3)*3
    bc = (c//3)*3
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if (i,j) != (r,c):
                neighbors.add((i,j))

    return neighbors

neighbors = {}
for cell in cells:
    neighbors[cell] = get_neighbors(*cell)

# ---------------- REVISE ----------------
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

    return revised, len(to_remove)

# ---------------- AC-3 ----------------
def AC3(domains):
    queue = deque()
    removed_count = 0

    # all arcs
    for Xi in cells:
        for Xj in neighbors[Xi]:
            queue.append((Xi, Xj))

    while queue:
        Xi, Xj = queue.popleft()

        revised, removed = revise(domains, Xi, Xj)
        removed_count += removed

        if revised:
            if len(domains[Xi]) == 0:
                return False, removed_count

            for Xk in neighbors[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))

    return True, removed_count


# ---------------- VISUALIZATION ----------------
def print_domain_sizes(domains):
    print("\nDomain Size Grid:")
    for r in range(9):
        row = []
        for c in range(9):
            row.append(str(len(domains[(r,c)])))
        print(" ".join(row))


# ---------------- DRIVER ----------------
domains_copy = copy.deepcopy(domains)

result, removed = AC3(domains_copy)

print("Total values removed:", removed)
print("Arc Consistent:", result)

print_domain_sizes(domains_copy)