#!/usr/bin/python3
import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(message):
    print(message)
    sys.exit(1)


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row=0, board=[]):
    """Backtracking function to place queens"""
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            solve_nqueens(n, row + 1, board + [col])


def main():
    """Main function to handle input validation and call the solver"""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")

    if N < 4:
        print_error_and_exit("N must be at least 4")

    solve_nqueens(N)


if __name__ == "__main__":
    main()
