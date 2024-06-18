#!/usr/bin/python3
import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error_and_exit():
    print("N must be a number")
    sys.exit(1)


def print_size_error_and_exit():
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col, N):
    """ Check if it's safe to place a queen at board[row][col] """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, N, solutions):
    """ Solve the N-Queens problem using backtracking """
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens(board, col + 1, N, solutions)
            board[i][col] = 0


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()

    if N < 4:
        print_size_error_and_exit()

    board = [[0] * N for _ in range(N)]
    solutions = []

    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
