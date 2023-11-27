"""

 The nqueens problem is of placing N queens on a N * N
 chess board such that no queen can attack any other queens placed
 on that chess board.
 This means that one queen cannot have any other queen on its horizontal, vertical and
 diagonal lines.

"""

from __future__ import annotations

solution: list[list[int]] = []


def is_safe(board: list[int], row: int, column: int) -> bool:
    """
    This function returns a boolean value True if
    it is safe to place a queen at the given row and column
    considering the current state of the board.

    :param board: The chessboard represented as a 1D list.
    :param row, column: Coordinates of the cell on the board.
    :return: True if it is safe to place a queen, False otherwise.

    >>> is_safe([0, 2, -1, -1], 2, 1)
    False
    >>> is_safe([0, -1, -1, -1], 1, 2)
    True
    """
    for i in range(row):
        if (
            board[i] == column
            or board[i] - i == column - row
            or board[i] + i == column + row
        ):
            return False
    return True


def solve(board: list[int], row: int) -> None:
    """
    Attempts to place queens on the board starting from the given row.

    :param board: The chessboard represented as a 1D list.
    :return row: The starting row from which to place queens.
    """
    if row >= len(board):
        solution.append(board.copy())
        printboard(board)
        print()
        return

    for i in range(len(board)):
        if is_safe(board, row, i):
            board[row] = i
            solve(board, row + 1)
            board[row] = -1  # Reset the state


def printboard(board: list[int]) -> None:
    """
    Prints the current state of the board.

    :param board: The chessboard represented as a 1D list.

    >>> printboard([0, 2, -1, -1])
    Q . . .
    . . Q .
    . . . .
    . . . .
    """
    n = len(board)
    for i in range(n):
        print(" ".join("Q" if board[i] == j else "." for j in range(n)))


if __name__ == "__main__":
    # Number of queens (e.g., n=8 for an 8x8 board)
    n = 8
    board = [0 for _ in range(n)]  # Place queens in the first column
    print("Initial board:")
    printboard(board)
    print("\nSolutions:")
    solve(board, 1)  # Start solving from the second row
    print("The total number of solutions are:", len(solution))
