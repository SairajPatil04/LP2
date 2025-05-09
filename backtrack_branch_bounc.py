def display_board(board):
    n = len(board)
    print("\nChessboard:")
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if board[row] == col else ". "
        print(line)
    print()


# ---------------------- Backtracking ----------------------
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens_backtrack(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve_nqueens_backtrack(board, row + 1, n):
                return True
            board[row] = -1  # Backtrack
    return False


# ---------------------- Branch and Bound ----------------------
def solve_nqueens_branch_bound(n):
    board = [-1] * n
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    def solve(row):
        if row == n:
            return True
        for col in range(n):
            if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                board[row] = col
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
                if solve(row + 1):
                    return True
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False
                board[row] = -1
        return False

    if solve(0):
        display_board(board)
    else:
        print("No solution exists.")


# ---------------------- Menu ----------------------
def main():
    while True:
        print("\n--- N-Queens Solver ---")
        print("1. Solve using Backtracking")
        print("2. Solve using Branch and Bound")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            n = int(input("Enter value of N: "))
            board = [-1] * n
            if solve_nqueens_backtrack(board, 0, n):
                print("\nSolution using Backtracking:")
                display_board(board)
            else:
                print("No solution found.")
        elif choice == '2':
            n = int(input("Enter value of N: "))
            print("\nSolution using Branch and Bound:")
            solve_nqueens_branch_bound(n)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
