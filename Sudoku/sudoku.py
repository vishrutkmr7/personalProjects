# I'll input a 9 x 9 matrix with numbers and _ for empty spaces. Return a matrix with the solution.
import itertools
from typing import List, Tuple, Optional


class Solution:
    def __init__(self):
        """
        Initializes the Solution class.

        Args:
            self: The Solution instance.

        Returns:
            None
        """
        self.board = None

    def solveSudoku(self, sudoku_board: List[List[str]]):
        """
        Solves the Sudoku puzzle.

        Args:
            sudoku_board: The Sudoku board represented as a 2D list of strings.

        Returns:
            None
        """
        self.board = sudoku_board
        self.solve()

    def find_empty(self) -> Optional[Tuple[int, int]]:
        """
        Finds the next empty cell in the Sudoku board.

        Args:
            self: The Solution instance.

        Returns:
            Optional[Tuple[int, int]]: The coordinates of the empty cell, or None if no empty cell is found.
        """
        return next(
            (
                (i, j)
                for i, j in itertools.product(range(9), range(9))
                if self.board[i][j] == "_"
            ),
            None,
        )

    def solve(self) -> bool:
        """
        Recursively solves the Sudoku puzzle.

        Args:
            self: The Solution instance.

        Returns:
            bool: True if the Sudoku puzzle is solved, False otherwise.
        """
        find = self.find_empty()
        if find is None:
            return True
        empty_row, empty_col = find
        for num in map(str, range(1, 10)):
            if self.valid(num, (empty_row, empty_col)):
                self.board[empty_row][empty_col] = num
                if self.solve():
                    return True
                self.board[empty_row][empty_col] = "_"
        return False

    def valid(self, num: str, pos: Tuple[int, int]) -> bool:
        """
        Checks if a number is valid in a given position of the Sudoku board.

        Args:
            num: The number to be checked.
            pos: The position to check the number in.

        Returns:
            bool: True if the number is valid in the given position, False otherwise.
        """
        # Check row
        if any(self.board[pos[0]][col] == num for col in range(9) if col != pos[1]):
            return False
        # Check column
        if any(self.board[row][pos[1]] == num for row in range(9) if row != pos[0]):
            return False
        # Check box
        box_x, box_y = pos[1] // 3, pos[0] // 3
        return not any(
            self.board[i][j] == num and (i, j) != pos
            for i, j in itertools.product(
                range(box_y * 3, box_y * 3 + 3), range(box_x * 3, box_x * 3 + 3)
            )
        )


if __name__ == "__main__":
    board = [
        ["_", "_", "_", "4", "_", "5", "_", "6", "1"],
        ["_", "_", "_", "_", "1", "_", "9", "_", "_"],
        ["5", "_", "_", "_", "2", "6", "_", "_", "_"],
        ["_", "_", "7", "_", "5", "8", "1", "_", "_"],
        ["3", "_", "_", "_", "_", "7", "_", "4", "_"],
        ["_", "_", "1", "_", "_", "_", "8", "9", "7"],
        ["_", "_", "9", "_", "8", "_", "_", "_", "_"],
        ["6", "_", "_", "3", "4", "_", "_", "2", "_"],
        ["_", "7", "_", "_", "_", "_", "_", "_", "3"],
    ]
    Solution().solveSudoku(board)
    # print grid
    for row in board:
        print(" ".join(str(cell) for cell in row))
