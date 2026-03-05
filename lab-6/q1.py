class heap:

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)//2
    
    def l_child(self,i):
        return 2*i+1
    
    def r_child(self,i):
        return 2*i+2
    
    def swap(self, l,r):
        self.heap[l],self.heap[r] = self.heap[r], self.heap[l]

    def push(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self, i):
        while i >0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i,self.parent(i))
            i = self.parent(i)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Empty Heap")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
    
    def heapify_down(self,i):
        smallest =i
        l = self.l_child(i)
        r = self.r_child(i)

        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        elif r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest =r

        if smallest != i:
            self.swap(smallest,i)
            self.heapify_down(smallest)

class Node:
    def __init__(self,s,p=None,a=None,c=0):
        self.state=s
        self.parent=p
        self.action=a
        self.cost=c

class Problem:
    def __init__(self,start,goal,graph,h):
        self.start=start
        self.goal=goal
        self.graph=graph
        self.h=h

    def goal_test(self,s):
        return s==self.goal

    def expand(self,node):
        res=[]
        for n in self.graph[node.state]:
            c=node.cost+self.graph[node.state][n]
            res.append(Node(n,node,n,c))
        return res

def path(node):
    p=[]
    while node:
        p.append(node.state)
        node=node.parent
    return p[::-1]

def greedy(prob):
    pq=heap()
    uid=0
    pq.push((prob.h[prob.start],uid,Node(prob.start)))
    seen=set()
    cnt=0
    while True:
        if len(pq.heap)==0:
            return None
        _,_,node=pq.pop()
        if node.state in seen:
            continue
        seen.add(node.state)
        cnt+=1
        if prob.goal_test(node.state):
            return path(node),cnt
        for ch in prob.expand(node):
            uid+=1
            pq.push((prob.h[ch.state],uid,ch))

def astar(prob):
   
    pq=heap()
    uid=0
    pq.push((prob.h[prob.start],uid,Node(prob.start)))
    seen=set()
    cnt=0
   
    while True:
   
        if len(pq.heap)==0:
            return None
        _,_,node=pq.pop()
        if node.state in seen:
            continue
        seen.add(node.state)
        cnt+=1
        if prob.goal_test(node.state):
            return path(node),cnt
        for ch in prob.expand(node):
            uid+=1
            f=ch.cost+prob.h[ch.state]
            pq.push((f,uid,ch))

h={'Boston':0,'Providence':50,'Portland':107,'New York':215,'Philadelphia':270,'Baltimore':360,'Syracuse':260,'Buffalo':400,'Pittsburgh':470,'Cleveland':550,'Columbus':640,'Detroit':610,'Indianapolis':780,'Chicago':860}

g={
'Chicago':{'Detroit':280,'Indianapolis':180},
'Detroit':{'Chicago':280,'Cleveland':170},
'Indianapolis':{'Chicago':180,'Columbus':175},
'Columbus':{'Indianapolis':175,'Cleveland':140,'Pittsburgh':185},
'Cleveland':{'Detroit':170,'Columbus':140,'Pittsburgh':135,'Buffalo':190},
'Pittsburgh':{'Columbus':185,'Cleveland':135,'Buffalo':215,'Philadelphia':305},
'Buffalo':{'Cleveland':190,'Pittsburgh':215,'Syracuse':150},
'Syracuse':{'Buffalo':150,'New York':250,'Boston':310},
'Philadelphia':{'Pittsburgh':305,'New York':95,'Baltimore':100},
'Baltimore':{'Philadelphia':100},
'New York':{'Philadelphia':95,'Providence':180,'Syracuse':250},
'Providence':{'New York':180,'Boston':50},
'Boston':{'Providence':50},
'Portland':{}
}

p=Problem('Chicago','Boston',g,h)

print(greedy(p))

print(astar(p))
        


    






    


    



        
        