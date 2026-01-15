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

def dfs(visited, curr, path_cost, end, dfs_costs, n, adj):
    if curr == end:
        dfs_costs.append(path_cost)
        return

    for i in range(n):
        if adj[curr][i] != float('inf'):
            if visited[i] == 0:
                visited[i] = 1
                dfs(visited, i, path_cost + adj[curr][i], end, dfs_costs, n, adj)
                visited[i] = 0

def bfs(adj, bfs_costs, st, end, n):
    visited = [False] * n
    visited[st] = True
    
    q = Queue()
    q.push((st, 0, visited))

    while not q.is_empty():
        data = q.pop()
        curr = data[0]
        cost = data[1]
        curr_visited = data[2]

        if curr == end:
            bfs_costs.append(cost)
            continue

        for i in range(n):
            if adj[curr][i] != float('inf') and not curr_visited[i]:
                # Create a copy of the visited list for the new path
                next_visited = list(curr_visited)
                next_visited[i] = True
                q.push((i, cost + adj[curr][i], next_visited))

def main():
    n = 14
    adj = [[float('inf')] * n for _ in range(n)]

    # City index mapping
    # 0  Chicago
    # 1  Detroit
    # 2  Cleveland
    # 3  Indianapolis
    # 4  Columbus
    # 5  Buffalo
    # 6  Pittsburgh
    # 7  Syracuse
    # 8  Philadelphia
    # 9  Baltimore
    # 10 New York
    # 11 Providence
    # 12 Boston
    # 13 Portland

    st = 0
    end = 7

    add_edge(adj, 0, 1, 283)
    add_edge(adj, 0, 2, 345)
    add_edge(adj, 0, 3, 182)

    add_edge(adj, 3, 4, 176)

    add_edge(adj, 4, 2, 144)
    add_edge(adj, 4, 6, 185)

    add_edge(adj, 2, 1, 169)
    add_edge(adj, 2, 5, 189)
    add_edge(adj, 2, 6, 134)

    add_edge(adj, 1, 5, 256)

    add_edge(adj, 5, 7, 150)
    add_edge(adj, 5, 6, 215)

    add_edge(adj, 6, 8, 305)
    add_edge(adj, 6, 9, 247)

    add_edge(adj, 9, 8, 101)

    add_edge(adj, 8, 10, 97)

    add_edge(adj, 10, 11, 181)
    add_edge(adj, 10, 12, 215)

    add_edge(adj, 12, 11, 50)
    add_edge(adj, 12, 13, 107)

    add_edge(adj, 7, 12, 312)
    add_edge(adj, 7, 8, 253)
    add_edge(adj, 7, 10, 254)

    dfs_costs = []
    visited = [0] * n
    visited[st] = 1
    
    dfs(visited, st, 0, end, dfs_costs, n, adj)

    for cost in dfs_costs:
        print(f"{cost} ,", end="")
    
    print(f"\n{len(dfs_costs)} dfs paths found")

    bfs_costs = []
    bfs(adj, bfs_costs, st, end, n)
    print(f"bfs paths: {len(bfs_costs)}")

if __name__ == "__main__":
    main()