import random
import math

N = 8

def random_board():
    return [random.randint(0,7) for _ in range(N)]

def heuristic(board):
    h = 0
    for i in range(N):
        for j in range(i+1, N):
            if board[i] == board[j]:
                h += 1
            if abs(board[i]-board[j]) == abs(i-j):
                h += 1
    return h

def best_neighbor(board):
    best = board[:]
    best_h = heuristic(board)
    
    for col in range(N):
        original_row = board[col]
        for row in range(N):
            if row == original_row:
                continue
            board[col] = row
            h = heuristic(board)
            if h < best_h:
                best_h = h
                best = board[:]
        board[col] = original_row
        
    return best, best_h

def steepest_ascent(board):
    steps = 0
    current = board[:]
    current_h = heuristic(current)
    
    while True:
        neighbor, nh = best_neighbor(current)
        if nh >= current_h:
            return current, current_h, steps
        current = neighbor
        current_h = nh
        steps += 1

results = []

for _ in range(50):
    b = random_board()
    h0 = heuristic(b)
    final, hf, steps = steepest_ascent(b)
    status = "Solved" if hf == 0 else "Fail"
    
    results.append((h0, hf, steps, status))

print("Run  Initial_h  Final_h  Steps  Status")
for i, r in enumerate(results, 1):
    print(f"{i:2d}   {r[0]:3d}       {r[1]:3d}     {r[2]:3d}   {r[3]}")

solved = sum(1 for r in results if r[3] == "Solved")
fail = len(results) - solved

print("\nSolved:", solved)
print("Failed:", fail)

for i, r in enumerate(results, 1):
    if r[1] > 0:
        print(f"\nLocal minimum encountered in run {i} with final heuristic =", r[1])
        print("This proves hill climbing got stuck at a non‑goal state with no better neighbor.")
        break