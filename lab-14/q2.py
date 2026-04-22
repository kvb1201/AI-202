# 2. Write a program to solve the questions using Backward Chaining.

# a. Knowledge Base:
# P → Q
# R → Q
# A → P
# B → R
# A
# B
# Conclusion:
# Q

# b. Knowledge Base:
# A → B
# B ∧ C → D
# E → C
# A
# E
# Conclusion:
# D

class KB:
    def __init__(self):
        self.symbols = []
        self.premise_conclusions = {}
        self.facts = []

    def take_input(self):
        print("Enter symbols in a single line separated by space: ")
        self.symbols = input().split()
        n = int(input("Enter number of premises: "))
        for i in range(n):
            premise = tuple(input(f"Enter {i+1}th premise: ").split())
            conclusion = input("Enter conclusion for it: ")
            self.premise_conclusions.update({premise: conclusion})

        self.facts = input("Enter facts separated by space: ").split()


def backward_chaining(KB, q):
    return or_search(q, KB, set())

def or_search(goal, KB, visited):

    if goal in KB.facts:
        return True
    if goal in visited:
        return False
    
    visited.add(goal)

    for premise in KB.premise_conclusions:
        if KB.premise_conclusions[premise] == goal:
            if and_search(premise, KB, visited.copy()) == True:
                return True
    return False


def and_search(premises, KB, visited):

    for p in premises:
        if or_search(p, KB, visited) == False:
            return False
        
    return True

kb = KB()
kb.take_input()
goal = input('Enter the goal: ')
print(backward_chaining(kb,goal))



    



        