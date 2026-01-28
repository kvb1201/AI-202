# Implement a Simple Reflex Agent for a vacuum cleaner that can navigate a three-room
# environment (A, B, and C) and maintain cleanliness. Identify the “rationality” of its
# actions. How will you define the performance cost? Define the complete Rule Table and
# store it either in a dictionary/vector/matrix based on the language you implement the
# vacuum cleaner. Show the simulation output with percept, action, and location. Do you
# need priorities in the rules?

import random
ruleTable = {
    ('A','DIRTY'):'SUCK',
    ('B', 'DIRTY'):'SUCK',
    ('C', 'DIRTY'):'SUCK',
    ('A','CLEAN'):'MOVE RIGHT',
    ('B','CLEAN'):random.choice(['MOVE RIGHT', 'MOVE LEFT']),
    ('C', 'CLEAN'): 'MOVE LEFT'
}


#Cost is associated for actions: move left, move right and suck

class VaccumAgent:
    def __init__(self):
        self.cost =0
    
    def perceive(self, location, room_status):
        return(location, room_status)
    
    def act(self, percept):
        if percept[0] =='B' and percept[1] == 'CLEAN':
            return random.choice(['MOVE LEFT', 'MOVE RIGHT'])
        else:
            return ruleTable.get(percept)
    

class Environment:



    def __init__(self):
        #environment initialized with rooms A,B and C all dirty 
        self.rooms = {'A':'DIRTY', 'B':'DIRTY', 'C':'DIRTY'} 
        self.location = 'A'

    
 
            

    def move(self, action):

        if action == 'MOVE RIGHT':
            if self.location == 'A':
                self.location = 'B'
            elif self.location == 'B':
                self.location = 'C'

        if action == 'MOVE LEFT':
            if self.location == 'C':
                self.location = 'B'
            elif self.location == 'B':
                self.location = 'A'
            
    def clean(self):
        self.rooms[self.location] = 'CLEAN'


def simulate(steps = 12):
        agent = VaccumAgent()
        env = Environment()
        print("Step\t Percept \tAction \tLocation")

        for step in range(steps):
            percept = agent.perceive(env.location, env.rooms[env.location])
            action = agent.act(percept)
            
            print(f"{step}\t{percept}\t{action}\t {env.location}")

            if action == 'SUCK':
                env.clean()
                agent.cost +=1
            elif action in ['MOVE LEFT', 'MOVE RIGHT']:
                env.move(action)
                agent.cost +=1

            else:
                break

        print('Cost: ',agent.cost)

    
simulate()

    




        
    

        