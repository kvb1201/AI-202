# 1. Write a program to solve the questions using Forward Chaining.
# a. Knowledge Base:
# P → Q
# L ∧ M → P
# A ∧ B → L
# A
# B
# M
# Conclusion:
# Q






from collections import deque,defaultdict

class KB1:

    def __init__(self):
        self.symbols = ['P','Q','L',"M", 'A', 'B']
        self.premise_conclusion = {('P',):'Q',
                              ('L','M'):'P',
                              ('A','B'):'L'}
        self.facts = ['A','B','M']


 

def foward_chaining(KB,q):
    inputs = KB
    inferred = {}
    for symbol in KB.symbols:
        inferred.update({symbol:False})

    count = defaultdict(int)
    for premise in KB.premise_conclusion:
        count[premise] = len(premise)
 

    queue = deque(KB.facts)
    conclusions = []

    while queue:
        p = queue.popleft()
        if p == q:
            return True
        
        if not inferred[p]:
            inferred[p] = True

        for premise in KB.premise_conclusion:
            if p in premise:
                count[premise]-=1
                if count[premise] == 0:
                    conclusion = KB.premise_conclusion[premise]
                    if not inferred[conclusion]:
                        conclusions.append(conclusion)
                        queue.append(conclusion)
                    


    return False


kb = KB1()
print("Result for A:",foward_chaining(kb,'Q'))



        
    
        

    





    
