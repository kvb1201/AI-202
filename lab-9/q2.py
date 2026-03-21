import math
def print_board(board):

    for i in range(0,9,3):
        print(board[i], "|" ,board[i+1], "|", board[i+2])
        if i <6:
            print("--+---+--")


def check_winner(board,player):

    win_states = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]

    for state in win_states:
        if all(board[i] == player for i in state):
            return True
    return False

def is_draw(board):
    return " " not in board


def minimax(board, depth, alpha, beta, maximizing):

    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    
    if is_draw(board):
        return 0
    
    if maximizing:
        max_eval = -float("inf")

        for i in range(9):

            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board,depth+1, alpha, beta,False)
                board[i] = " "
                max_eval = max(eval, max_eval)
                alpha = max(alpha,max_eval)

                if alpha >= beta:
                    break

        return max_eval
    
    else:
        min_eval = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth+1, alpha, beta, True)
                board[i] = " "

                min_eval = min(eval, min_eval)
                beta = min(beta, min_eval)

                if alpha >= beta:
                    break

        return min_eval
    
def best_move(board):
    best_val = -float("inf")
    move = -1

    for i in range(9):
        if board[i] ==" ":
            board[i] = "O"
            move_val = minimax(board,0, -float("inf"), float("inf"), False)
            board[i] = " "

            if move_val > best_val:
                best_val = move_val
                move = i

    return move


board = [" " for i in range(9)]

while True:
    print_board(board)

    move = int(input("Enter possible position 0-8: "))
    possible_moves = [i for i in range(9)]

    if move not in possible_moves or board[move] != " ":
        print("Invalid Move !")
        continue

    board[move] = "X"

    if check_winner(board, "X"):
        print("You won!")
        break

    if check_winner(board, "O"):
        print("Computer won !")
        break

    if is_draw(board):
        print("Draw !")
        break

    ai_move = best_move(board)
    board[ai_move] = "O"

    if check_winner(board, "O"):
        print_board(board)
        print("AI wins!")
        break

    if is_draw(board):
        print_board(board)
        print("Draw!")
        break





    





