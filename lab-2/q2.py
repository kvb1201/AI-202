import sys
sys.setrecursionlimit(300000)


class Queue:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def empty(self):
        if(len(self.items) == 0):
            return True
        else:
            return False 

    def pop(self):
        if(self.empty()):
            print('Empty Queue')
            return None
        else:
            self.items.pop(0)
            return None
    
    def front(self):
        if(self.empty()):
            return None
        else:
            return self.items[0]


start_state =((7,2,4),
              (5,'_',6),
              (8,3,1))

final_state = (('_',1,2),
               (3,4,5),
               (6,7,8))


def check_solvable(matrix):
    flatten_matrix = []
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == '_':
                continue
            else:
                flatten_matrix.append(matrix[i][j])

    count =0
    for i in range(8):
        for j in range(i+1,8):
            if flatten_matrix[i] > flatten_matrix[j]:
                count+=1
    return count%2==0

def find_(matrix):
    
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == '_':
                return (i,j)
            

def generate_states(matrix):
    x,y = find_(matrix)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    states = []

    for dx, dy in directions:
        nx,ny = x+dx, y+dy

        if 0<=nx<3 and 0<=ny<3:
            new_state = [list(row) for row in matrix]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            states.append(tuple(tuple(row) for row in new_state))

    return states

def dfs(start_state, goal_state, visited, explored):
    if start_state in visited:
        return False

    visited.add(start_state)
    explored[0] += 1   

    if start_state == goal_state:
        return True

    for state in generate_states(start_state):
        if dfs(state, goal_state, visited, explored):
            return True

    return False
    
visited = set()
explored = [0]   

if check_solvable(start_state):
    dfs(start_state, final_state, visited, explored)
    print(explored[0])
else:
    print("Not solvable")

