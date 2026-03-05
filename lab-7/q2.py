

import random
import math

N = 8

def random_board():
    return [random.randint(0, 7) for _ in range(N)]

def heuristic(board):
    h = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:
                h += 1
            if abs(board[i] - board[j]) == abs(i - j):
                h += 1
    return h

def best_neighbor(board):
    best = board[:]
    best_h = heuristic(board)

    for col in range(N):
        orig = board[col]
        for row in range(N):
            if row == orig:
                continue
            board[col] = row
            h = heuristic(board)
            if h < best_h:
                best_h = h
                best = board[:]
        board[col] = orig

    return best, best_h

def steepest_ascent(board):
    current = board[:]
    h = heuristic(current)
    steps = 0

    while True:
        nb, nh = best_neighbor(current)
        if nh >= h:
            return current, h, steps
        current, h = nb, nh
        steps += 1

def first_choice(board):
    current = board[:]
    h = heuristic(current)
    steps = 0

    while True:
        improved = False
        for _ in range(100):
            col = random.randint(0, 7)
            row = random.randint(0, 7)
            if row == current[col]:
                continue
            new = current[:]
            new[col] = row
            nh = heuristic(new)
            if nh < h:
                current, h = new, nh
                steps += 1
                improved = True
                break
        if not improved:
            return current, h, steps

def random_restart(max_restarts=100):
    total_steps = 0
    for _ in range(max_restarts):
        b = random_board()
        final, h, steps = steepest_ascent(b)
        total_steps += steps
        if h == 0:
            return final, h, total_steps
    return final, h, total_steps

def simulated_annealing(board):
    current = board[:]
    h = heuristic(current)
    T = 1.0
    cooling = 0.99
    steps = 0

    while T > 0.001 and h > 0:
        col = random.randint(0, 7)
        row = random.randint(0, 7)
        new = current[:]
        new[col] = row
        nh = heuristic(new)
        delta = nh - h

        if delta < 0 or random.random() < math.exp(-delta / T):
            current, h = new, nh

        T *= cooling
        steps += 1

    return current, h, steps

def run_method(name, solver, runs=50):
    results = []
    for _ in range(runs):
        b = random_board()
        h0 = heuristic(b)

        if name == "Random Restart":
            final, hf, steps = solver()
        else:
            final, hf, steps = solver(b)

        status = "Solved" if hf == 0 else "Fail"
        results.append((h0, hf, steps, status))

    solved = sum(1 for r in results if r[3] == "Solved")
    fail = runs - solved

    print(f"\n=== {name} ===")
    print("Run  Initial_h  Final_h  Steps  Status")
    for i, r in enumerate(results, 1):
        print(f"{i:2d}   {r[0]:3d}       {r[1]:3d}     {r[2]:3d}   {r[3]}")
    print("Solved:", solved)
    print("Failed:", fail)

if __name__ == "__main__":
    run_method("First Choice", first_choice)
    run_method("Random Restart", random_restart)
    run_method("Simulated Annealing", simulated_annealing)