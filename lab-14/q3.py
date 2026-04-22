# 3. Write a program to solve the questions using the method Resolution and proof of
# refutation/contradiction.

# a. Knowledge Base:
# P ∨ Q
# P → R
# Q → S
# R → S
# Conclusion
# S
# b. Knowledge Base:
# P → Q
# Q → R
# S → ¬R
# P
# Conclusion:
# S


kb1 = [
    {'P','Q'},
    {'~P':'R'},
    {'~Q':'S'},
    {'~R':'S'}
]

kb2 = [
    {"~P", "Q"},
    {"~Q", "R"},
    {"~S", "~R"},
    {"P"}
]


def negate(literal):
    return literal[1:] if literal[0] == '~' else '~' + literal


def resolve(c1,c2):
    resolvents = []
    for literal in c1:
        if negate(literal) in c2:
            new_clause = (c1- {literal}) | (c2 - {negate(literal) })
            resolvents.append(frozenset(new_clause))
    return resolvents



def resolution(KB, query):
    clauses = set(frozenset(c) for c in KB)
    clauses.add(frozenset([negate(query)]))

    while True:
        new = set()
        clauses_list = list(clauses)

        for i in range(len(clauses_list)):
            for j in range(i+1, len(clauses_list)):
                resolvents = resolve(clauses_list[i], clauses_list[j])

                for r in resolvents:
                    if len(r) == 0:
                        return True
                    new.add(r)
                
        if new.issubset(clauses):
            return False
        
        clauses = clauses.union(new)


print("Case (a):", resolution(kb1, "S"))
print("Case (b):", resolution(kb2, "S"))

            

            

                




