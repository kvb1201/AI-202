class minHeap:
    def __init__(self):
        self.heap = []

    def parent(self,i):
        return (i-1)//2
    
    def left(self, i):
        return 2*i+1
    
    def right(self, i):
        return 2*i+2
    
    def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j], self.heap[i]

    def push(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self,index):
        while index >0 and self.heap[self.parent(index)] > self.heap[index]:
            self.swap(index,self.parent(index))
            index = self.parent(index)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Empty Heap")

        root = self.heap[0]

        if len(self.heap) == 1:
            self.heap.pop()
            return root

        # move last element to root, then heapify down
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
    
    def heapify_down(self,index):
        smallest = index
        left = self.left(index)
        right = self.right(index)

        if left < len(self.heap) and self.heap[smallest] > self.heap[left]:
            smallest = left
        
        if right < len(self.heap) and self.heap[smallest] > self.heap[right]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)

            self.heapify_down(smallest)

    def peek(self):
        if not self.heap:
            raise IndexError("Empty Heap")
        return self.heap[0]
        
    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) ==0
    

    """
0 = free corridor
1 = wall/room (blocked)
S = Entry (start)
G = Exit (goal)


    """

grid = [
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,0,0,1],
    [1,0,1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1]
]
moves = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

class Node:

    def __init__(self,state, parent = None, path_cost =0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost

    def __lt__(self,other):
        return self.path_cost < other.path_cost
        

def get_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def best_first_search(grid, start, goal):
    frontier = minHeap()
    reached = {}
    rows,cols = len(grid), len(grid[0])

    start_node = Node(start, None, 0)
    frontier.push((0,start_node))
    reached[start] = 0

    while not frontier.is_empty():
        cost,node = frontier.pop()

        print(f"Exploring: {node.state}, Cost so far: {node.path_cost} ")

        if node.state == goal:
            print("Exit Reached")
            return get_path(node),cost
        
        for dx, dy in moves:
            new_x, new_y = node.state[0] + dx, node.state[1] + dy

            if 0 <= new_x < rows and 0 <= new_y < cols:
                if grid[new_x][new_y] != 1:
                    new_cost = node.path_cost +1
                    if (new_x,new_y) not in reached or new_cost < reached[(new_x,new_y)]:
                        reached[(new_x,new_y)] = new_cost
                        new_node = Node((new_x,new_y), node, new_cost )
                        frontier.push((new_cost,new_node))

    return None, float("inf")
    

start = (3,3)
goal = (1,10)

path,cost = best_first_search(grid, start, goal)
print("Evacuation Route", path)
print("Total steps:", cost)







    

 
    
        
        
        