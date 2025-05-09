import math

# Check if the current board configuration is valid
def is_valid(board, row, col, n):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

# Bound function (to check if we can still extend a solution)
def bound(board, row, n):
    return row < n

# Backtracking function (pure backtracking, without any bounding)
def backtrack_n_queens(board, row, n):
    if row == n:  # All queens are placed
        return True
    
    for col in range(n):
        if is_valid(board, row, col, n):  # If it's safe to place the queen
            board[row] = col  # Place queen
            
            if backtrack_n_queens(board, row + 1, n):  # Recursively place queens
                return True  # If placing the queen leads to a solution, return True
            
            board[row] = -1  # Backtrack (remove the queen)
    
    return False  # No solution found

# Branch and Bound approach
def branch_and_bound_n_queens(board, row, n):
    if row == n:  # All queens are placed
        return True
    
    for col in range(n):
        if is_valid(board, row, col, n):  # If it's safe to place the queen
            board[row] = col  # Place queen
            
            if bound(board, row, n) and branch_and_bound_n_queens(board, row + 1, n):
                return True  # If placing the queen leads to a solution, return True
            
            board[row] = -1  # Backtrack
    
    return False  # No solution found

# Function to print the solution
def print_solution(board, n):
    for row in range(n):
        print(' '.join('Q' if col == board[row] else '.' for col in range(n)))

# Main function to solve N-Queens using Branch and Bound
def n_queens_branch_bound(n):
    board = [-1] * n  # Initialize an empty board
    if branch_and_bound_n_queens(board, 0, n):
        print_solution(board, n)
    else:
        print("Solution does not exist")

# Main function to solve N-Queens using Backtracking
def n_queens_backtracking(n):
    board = [-1] * n  # Initialize an empty board
    if backtrack_n_queens(board, 0, n):
        print_solution(board, n)
    else:
        print("Solution does not exist")

# Example: Solve for 4 Queens using Branch and Bound
print("Branch and Bound Solution for 4 Queens:")
n_queens_branch_bound(4)

# Example: Solve for 4 Queens using Backtracking
print("\nBacktracking Solution for 4 Queens:")
n_queens_backtracking(4)
