class Node:

    def __init__(self, state, parent= None,action= None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

    def __repr__(self):
        return f"Node(state = {self.state}, depth = {self.depth}) "

class problem:

    def __init__(self):
        
        self.initial = (3,3,'L')

    def is_goal(self,state):
        return state == (0,0,'R')
    
    def depth(self, node):
        return node.depth
    
    def is_cycle(self,node):

        temp = node.parent
        while temp:
            if temp.state == node.state:
                return True
            temp = temp.parent
        
        return False
    
    def is_valid(self, state):
        g_left,b_left,boat = state
        g_right = 3-g_left
        b_right = 3-b_left
        left_check = (g_left ==0) or (g_left>= b_left)
        right_check = (g_right == 0) or (g_right >= b_right)

        return left_check and right_check
    
    def expand(self, node):
        G,B,boat = node.state

        if boat == 'L':
            direction = -1
        else:
            direction = 1
        
        possible_transfer = [
            (1,0),
            (0,1),
            (1,1),
            (2,0),
            (0,2)
        ]

        children = []

        for g,b in possible_transfer:
            new_g = G + g*direction
            new_b = B + b*direction
            new_boat = 'L' if boat == 'R' else 'R'

            new_state = (new_g,new_b,new_boat)

            if 0 <= new_g <=3 and 0<= new_b <= 3 and self.is_valid(new_state):
                child_node=Node(new_state, node, action=(g,b,boat + "->" + new_boat) , depth= node.depth +1)

                children.append(child_node)

        return children
    

def dls(problem,limit):
    frontier = [Node(problem.initial, None, None, 0)]
    result = "Failure"

    while frontier:
        node = frontier.pop()

        if problem.is_goal(node.state):
            return node
        
        if problem.depth(node) > limit:
            result = "cutoff"

        else:
            if not problem.is_cycle(node):
                for child in problem.expand(node):
                    frontier.append(child)

    return result
    
def iterative_deepening_search(problem):
    depth =0

    while True:
        print(f"searching at depth limit= {depth}")
        result = dls(problem,depth)
        print(result)

        if result != "cutoff":
            return result
        
        depth +=1



def print_solution(node):
    path = []
    while node:
        path.append((node.state,node.action))
        node = node.parent

    path.reverse()

    print("\nSolution Path:")

    for i, (state,action) in enumerate(path):
        print(f"step: {i}, state = {state}, action = {action}")

    
if __name__ == "__main__":
    problem = problem()
    solution = dls(problem,3)
    print("Solution of dls with limit 3: ",solution)

    solution = iterative_deepening_search(problem)

    if solution == "Failure":
        print("No solution found")

    else:
        print_solution(solution)


                









        