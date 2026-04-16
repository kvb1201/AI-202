import itertools

class Symbol:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


# logical operations
def NOT(p): return not p
def AND(*args): return all(args)
def OR(*args): return any(args)
def IMPLIES(p, q): return (not p) or q
def IFF(p, q): return p == q


# evaluate expressions
def evaluate(expr, values):
    return eval(expr, {
        "NOT": NOT,
        "AND": AND,
        "OR": OR,
        "IMPLIES": IMPLIES,
        "IFF": IFF
    }, values)


# print truth table
def truth_table(expr, symbols):
    names = [s.name for s in symbols]
    print(" | ".join(names) + " | " + expr)
    print("-" * (len(names)*4 + len(expr)))

    for vals in itertools.product([False, True], repeat=len(symbols)):
        env = dict(zip(names, vals))
        result = evaluate(expr, env)
        row = ["T" if v else "F" for v in vals]
        print(" | ".join(row) + " | " + ("T" if result else "F"))


# symbols
P = Symbol('P')
Q = Symbol('Q')
R = Symbol('R')


# expressions
expressions = [
    ("IMPLIES(NOT(P), Q)", [P, Q]),
    ("AND(NOT(P), NOT(Q))", [P, Q]),
    ("OR(NOT(P), NOT(Q))", [P, Q]),
    ("IMPLIES(NOT(P), NOT(Q))", [P, Q]),
    ("IFF(NOT(P), NOT(Q))", [P, Q]),
    ("AND(OR(P, Q), IMPLIES(NOT(P), Q))", [P, Q]),
    ("IMPLIES(OR(P, Q), NOT(R))", [P, Q, R]),
    ("IFF(IMPLIES(OR(P, Q), NOT(R)), IMPLIES(AND(NOT(P), NOT(Q)), NOT(R)))", [P, Q, R]),
    ("IMPLIES(AND(IMPLIES(P, Q), IMPLIES(Q, R)), IMPLIES(Q, R))", [P, Q, R]),
    ("IMPLIES(IMPLIES(P, OR(Q, R)), AND(NOT(P), NOT(Q), NOT(R)))", [P, Q, R])
]


# run all
for expr, syms in expressions:
    print("\n")
    truth_table(expr, syms)