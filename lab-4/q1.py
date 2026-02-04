class minHeap:
    def __init__(self):
        self.heap = []

    def parent(self,i):
        return (i-1)//2
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

    def push(self,value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) -1)

    def _heapify_up(self,index):
        while index>0 and self.heap[self.parent(index)] >self.heap[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def pop(self):
        if len(self.heap)==0:
            raise IndexError("Heap is Empty")
        
        if len(self.heap)==1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_down(self,index):
        smallest = index
        left = self.left(index)
        right = self.right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] <self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.swap(index,smallest)
            self._heapify_down(smallest)

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    


graph = {
    "Chicago": [("Detroit",283), ("Cleveland",345), ("Indianapolis",182)],
    "Detroit": [("Chicago",283), ("Cleveland",169), ("Buffalo",256)],
    "Cleveland": [("Chicago",345), ("Detroit",169), ("Buffalo",189), ("Pittsburgh",134), ("Columbus",144)],
    "Indianapolis": [("Chicago",182), ("Columbus",176)],
    "Columbus": [("Indianapolis",176), ("Cleveland",144), ("Pittsburgh",185)],
    "Buffalo": [("Detroit",256), ("Cleveland",189), ("Pittsburgh",215), ("Syracuse",150)],
    "Pittsburgh": [("Cleveland",134), ("Columbus",185), ("Buffalo",215), ("Syracuse",253), ("Philadelphia",305), ("Baltimore",247)],
    "Syracuse": [("Buffalo",150), ("Pittsburgh",253), ("New York",254), ("Boston",312)],
    "New York": [("Syracuse",254), ("Philadelphia",97), ("Boston",215), ("Providence",181)],
    "Philadelphia": [("New York",97), ("Pittsburgh",305), ("Baltimore",101), ("Providence",215)],
    "Baltimore": [("Pittsburgh",247), ("Philadelphia",101)],
    "Boston": [("Syracuse",312), ("New York",215), ("Providence",50), ("Portland",107)],
    "Providence": [("Boston",50), ("New York",181), ("Philadelphia",215)],
    "Portland": [("Boston",107)]
}

start = "Syracuse"
goal = "Chicago"

class Node:
    def __init__(self, state, parent = None, path_cost =0):
       self.state = state
       self.parent = parent
       self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost
    

def get_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]
    

def best_first_search(graph,start,goal):
    frontier = minHeap()
    reached = {}

    start_node = Node(start, None, 0)
    frontier.push((0,start_node))
    reached[start] = 0

    while not frontier.is_empty():
        cost, node = frontier.pop()

        print(f"Exploring: {node.state}, cost so far: {cost}")

        if node.state == goal:
            print("Goal Found")
            return get_path(node), cost

        for neighbor, step_cost in graph[node.state]:
            new_cost = step_cost + node.path_cost

            if neighbor not in reached or new_cost < reached[neighbor]:
                reached[neighbor] = new_cost
                child_node = Node(neighbor, node, new_cost)
                frontier.push((new_cost, child_node))


path, cost = best_first_search(graph, start, goal)
print("Path", path)
print("Total Cost", cost) 



     





