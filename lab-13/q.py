# generate all combinations without itertools
def generate_combinations(n):
    if n == 0:
        return [[]]
    
    prev = generate_combinations(n - 1)
    result = []
    
    for p in prev:
        result.append(p + [False])
        result.append(p + [True])
    
    return result

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


# manual evaluate without using eval
def evaluate(expr, values):
    expr = expr.strip()

    # if variable
    if expr in values:
        return values[expr]

    # if NOT
    if expr.startswith("NOT("):
        inner = expr[4:-1]
        return NOT(evaluate(inner, values))

    # function with arguments
    def split_args(s):
        args = []
        depth = 0
        current = ""
        for ch in s:
            if ch == ',' and depth == 0:
                args.append(current.strip())
                current = ""
            else:
                if ch == '(':
                    depth += 1
                elif ch == ')':
                    depth -= 1
                current += ch
        if current:
            args.append(current.strip())
        return args

    # AND
    if expr.startswith("AND("):
        inner = expr[4:-1]
        args = split_args(inner)
        return AND(*[evaluate(a, values) for a in args])

    # OR
    if expr.startswith("OR("):
        inner = expr[3:-1]
        args = split_args(inner)
        return OR(*[evaluate(a, values) for a in args])

    # IMPLIES
    if expr.startswith("IMPLIES("):
        inner = expr[8:-1]
        p, q = split_args(inner)
        return IMPLIES(evaluate(p, values), evaluate(q, values))

    # IFF
    if expr.startswith("IFF("):
        inner = expr[4:-1]
        p, q = split_args(inner)
        return IFF(evaluate(p, values), evaluate(q, values))


# print truth table
def truth_table(expr, symbols):
    names = [s.name for s in symbols]
    print(" | ".join(names) + " | " + expr)
    print("-" * (len(names)*4 + len(expr)))

    for vals in generate_combinations(len(symbols)):
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