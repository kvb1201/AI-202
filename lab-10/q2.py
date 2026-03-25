# You are building a vacuum cleaning agent that can clean the floor tiles. You are given a
# simple setting of cleaning two tiles A and B where each percept contains two inputs of
# the location and state of the tile. But the agent goes erratic in the following ways:
# a. When applied to a dirty square the action cleans the square and sometimes
# cleans up dirt in an adjacent square, too.
# b. When applied to a clean square the action sometimes deposits dirt on the carpet.
# Design this erratic agent with AND-OR graph search algorithm.


class problem:

    def is_goal(self,state):
        return state in [('A','C','C'), ('B', 'C', 'C')]
    
    def initial(self):
        return ('A','D','D')
    
    def actions(self, state):
        pos,A,B = state

        acts = ['Suck']

        if pos == 'A':
            acts.append('Right')
        else:
            acts.append('Left')

        return acts
    
    def results(self, state, action):
        pos, A, B = state

        if action == 'Suck':
            if pos == 'A':
                if A == 'D':
                    return [('A', 'C', B), ('A', 'C', 'C')]
                else:
                    return [state, ('A','D',B)]
                
            if pos == 'B':
                if B == 'D':
                    return [('B', A, 'C'), ('B', 'C', 'C')]
                else:
                    return [state, ('B', A, 'D')]
                
        elif action == 'Left':
            return [('A',A,B)]
        elif action == 'Right':
            return [('B',A,B)]
        
def is_cycle(state, path):
    return state in path

def and_or_search(problem):
    return or_search(problem, problem.initial(), [])

def or_search(problem, state, path):
    if problem.is_goal(state):
        return []
    if is_cycle(state,path):
        return "failure"
    
    for action in problem.actions(state):
        plan = and_search(problem, problem.results(state,action), path + [state])
        if plan != 'failure':
            return [action,plan]
    return 'failure'
    
def and_search(problem, states, path):
    plans = {}
    for state in states:
        plan = or_search(problem, state, path)

        if plan == "failure":
            return "failure"
        
        plans[state] =plan

    return plans
        


if __name__ == "__main__":
    p = problem()
    print(and_or_search(p))
        
    
       




        


            
                
            
            

        


            

        

    



