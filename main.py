import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, mark):
    # Check rows, columns, and diagonals
    return any(
        all(cell == mark for cell in row) for row in board
    ) or any(
        all(row[i] == mark for row in board) for i in range(3)
    ) or all(
        board[i][i] == mark for i in range(3)
    ) or all(
        board[i][2 - i] == mark for i in range(3)
    )

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("This spot is already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

def computer_move(board):
    while True:
        move = random.randint(0, 8)
        row, col = divmod(move, 3)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            break

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        player_move(board)
        if check_win(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        computer_move(board)
        if check_win(board, 'O'):
            print_board(board)
            print("Computer wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

play_game()
