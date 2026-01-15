import sys

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

def add_edge(adj, u, v, d):
    adj[u][v] = d
    adj[v][u] = d

def bfs(adj, bfs_tree, st, n):
    visited = [False] * n
    visited[st] = True
    q = Queue()
    q.push(st)

    parent = [-1] * n
    
    while not q.is_empty():
        curr = q.pop()

        for j in range(n):
            if adj[curr][j] != float('inf') and not visited[j]:
                visited[j] = True
                parent[j] = curr
                q.push(j)

    for i in range(n):
        if parent[i] != -1:
            bfs_tree.append([parent[i], i])

def dfs(adj, dfs_tree, curr, visited, n):
    visited[curr] = True
    for i in range(n):
        if adj[curr][i] != float('inf') and not visited[i]:
            dfs_tree.append([curr, i])
            dfs(adj, dfs_tree, i, visited, n)

def main():
    n = 13
    adj = [[float('inf')] * n for _ in range(n)]

    # Name index mapping
    # 0  Raj
    # 1  Priya
    # 2  Aarav
    # 3  Neha_1   (center-left Neha)
    # 4  Neha_2   (right Neha)
    # 5  Akash
    # 6  Sunil
    # 7  Sneha
    # 8  Rahul
    # 9  Arjun_1 (right Arjun)
    # 10 Arjun_2 (bottom Arjun)
    # 11 Pooja
    # 12 Maya

    st = 0

    add_edge(adj, 0, 1, 1)
    add_edge(adj, 1, 2, 1)
    add_edge(adj, 0, 6, 1)
    add_edge(adj, 6, 5, 1)
    add_edge(adj, 5, 3, 1)
    add_edge(adj, 1, 3, 1)
    add_edge(adj, 3, 8, 1)
    add_edge(adj, 7, 8, 1)
    add_edge(adj, 6, 7, 1)
    add_edge(adj, 2, 4, 1)
    add_edge(adj, 4, 9, 1)
    add_edge(adj, 9, 8, 1)
    add_edge(adj, 8, 11, 1)
    add_edge(adj, 10, 11, 1)
    add_edge(adj, 10, 12, 1)
    add_edge(adj, 12, 8, 1)

    bfs_tree = []
    bfs(adj, bfs_tree, st, n)

    print("bfsTree")
    for level in bfs_tree:
        for val in level:
            print(f"{val},", end="")
        print()

    dfs_tree = []
    visited = [False] * n
    dfs(adj, dfs_tree, 0, visited, n)

    print("\n DFSTREE")
    for level in dfs_tree:
        for val in level:
            print(f"{val},", end="")
        print()

if __name__ == "__main__":
    main()