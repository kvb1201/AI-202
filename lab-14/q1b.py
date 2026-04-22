# b. Knowledge Base:
# A → B
# B → C
# C → D
# A
# E
# D ∧ E → F
# Conclusion: F


from collections import defaultdict, deque

class KB:

    def __init__(self):
        self.symbols = ['A','B','C','D','E','F']
        self.premise_conclusions = {
            ('A',):'B',
            ('B',):'C',
            ('C',):'D',
            ('D','E'):'F'
        }
        self.facts = ['A','E']



def foward_chaining(KB, q):

    inferred = {}
    for symbol in KB.symbols:
        inferred.update({symbol:False})

    queue = deque(KB.facts)

    count = defaultdict(int)

    for premise in KB.premise_conclusions:
        count[premise] = len(premise)

    while queue:
        p = queue.popleft()
        if p == q:
            return True
        
        if not inferred[p]:
            inferred[p] = True

        for premise in KB.premise_conclusions:
            if p in premise:
                count[premise] -=1
                if count[premise] == 0:
                    queue.append(KB.premise_conclusions[premise])

    
    return False


kb = KB()
print("Output for B, Deduced: ",foward_chaining(kb,'F'))