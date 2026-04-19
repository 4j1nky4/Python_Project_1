from termcolor import colored

x = 'X'
o = 'O'

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def cell(mark):
    if mark == x:
        return colored(x, 'red')
    elif mark == o:
        return colored(o, 'blue')
    else:
        return ' '
    
def print_board():
    print("\n")
    for row in board:
        print(" | ".join(cell(mark) for mark in row))
        print("-" * 9)
    print("\n")

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_board_full():
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    current_player = x
    while True:
        print_board()
        move = input(f"Player {current_player}, enter your move (row and column): ")
        try:
            row, col = map(int, move.split())
            if board[row][col] == ' ':
                board[row][col] = current_player
                winner = check_winner()
                if winner:
                    print_board()
                    print(f"Player {winner} wins!")
                    break
                elif is_board_full():
                    print_board()
                    print("It's a draw!")
                    break
                current_player = o if current_player == x else x
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as numbers between 0 and 2.")
if __name__ == "__main__":
    main()

