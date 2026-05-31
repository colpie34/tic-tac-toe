def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def get_number(board):
    while True:
        try:
            number = int(input("Choose a box (1-9): "))
            if number not in range(1, 10):
                print("Number Must Be Between 1 and 9.")
                continue
            if board[number - 1] in ["X", "O"]:
                print("That Box is already occupied")
                continue
            return number - 1
        except ValueError:
            print("Please enter a valid number")


def check_win(board, player):
    winning_combinations = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6),             # Diagonals
    )
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def check_tie(board):
    return all(square in ['X', 'O'] for square in board)


def tic_tac_toe():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        move = get_number(board)

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()