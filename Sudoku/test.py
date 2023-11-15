import pytest
from sudoku import Solution


# Test cases for solveSudoku method
@pytest.mark.parametrize(
    "test_input, expected_output, test_id",
    [
        # Happy path tests
        (
            [
                ["5", "3", "_", "_", "7", "_", "_", "_", "_"],
                ["6", "_", "_", "1", "9", "5", "_", "_", "_"],
                ["_", "9", "8", "_", "_", "_", "_", "6", "_"],
                ["8", "_", "_", "_", "6", "_", "_", "_", "3"],
                ["4", "_", "_", "8", "_", "3", "_", "_", "1"],
                ["7", "_", "_", "_", "2", "_", "_", "_", "6"],
                ["_", "6", "_", "_", "_", "_", "2", "8", "_"],
                ["_", "_", "_", "4", "1", "9", "_", "_", "5"],
                ["_", "_", "_", "_", "8", "_", "_", "7", "9"],
            ],
            True,
            "happy_path_solved",
        ),
        # Edge cases
        (
            [
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ],
            True,
            "edge_case_empty_board",
        ),
        # Error cases
        (
            [
                ["5", "3", "5", "_", "7", "_", "_", "_", "_"],
                ["6", "_", "_", "1", "9", "5", "_", "_", "_"],
                ["_", "9", "8", "_", "_", "_", "_", "6", "_"],
                ["8", "_", "_", "_", "6", "_", "_", "_", "3"],
                ["4", "_", "_", "8", "_", "3", "_", "_", "1"],
                ["7", "_", "_", "_", "2", "_", "_", "_", "6"],
                ["_", "6", "_", "_", "_", "_", "2", "8", "_"],
                ["_", "_", "_", "4", "1", "9", "_", "_", "5"],
                ["_", "_", "_", "_", "8", "_", "_", "7", "9"],
            ],
            False,
            "error_case_invalid_board",
        ),
    ],
)
def test_solveSudoku(test_input, expected_output, test_id):
    # Arrange
    solution = Solution()

    # Act
    solution.solveSudoku(test_input)
    result = all(all(cell != "_" for cell in row) for row in solution.board)

    # Assert
    assert result == expected_output, f"Test failed for test_id: {test_id}"
    print(f"Test passed for test_id: {test_id}")


# Test cases for find_empty method
@pytest.mark.parametrize(
    "board, expected_output, test_id",
    [
        # Happy path tests
        (
            [
                ["5", "3", "_", "_", "7", "_", "_", "_", "_"],
                ["6", "_", "_", "1", "9", "5", "_", "_", "_"],
                ["_", "9", "8", "_", "_", "_", "_", "6", "_"],
                ["8", "_", "_", "_", "6", "_", "_", "_", "3"],
                ["4", "_", "_", "8", "_", "3", "_", "_", "1"],
                ["7", "_", "_", "_", "2", "_", "_", "_", "6"],
                ["_", "6", "_", "_", "_", "_", "2", "8", "_"],
                ["_", "_", "_", "4", "1", "9", "_", "_", "5"],
                ["_", "_", "_", "_", "8", "_", "_", "7", "9"],
            ],
            (0, 2),
            "happy_path_first_empty",
        ),
        # Edge cases
        (
            [
                ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
            ],
            None,
            "edge_case_no_empty",
        ),
        # Error cases are not applicable for find_empty method as it does not raise exceptions
    ],
)
def test_find_empty(board, expected_output, test_id):
    # Arrange
    solution = Solution()
    solution.board = board

    # Act
    result = solution.find_empty()

    # Assert
    assert result == expected_output, f"Test failed for test_id: {test_id}"
    print(f"Test passed for test_id: {test_id}")


# Test cases for valid method
@pytest.mark.parametrize(
    "num, pos, board, expected_output, test_id",
    [
        # Happy path tests
        (
            "5",
            (0, 2),
            [
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ],
            True,
            "happy_path_valid_number",
        ),
        # Edge cases
        (
            "5",
            (0, 2),
            [
                ["5", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ],
            False,
            "edge_case_invalid_row",
        ),
        # Error cases are not applicable for valid method as it does not raise exceptions
    ],
)
def test_valid(num, pos, board, expected_output, test_id):
    # Arrange
    solution = Solution()
    solution.board = board

    # Act
    result = solution.valid(num, pos)

    # Assert
    assert result == expected_output, f"Test failed for test_id: {test_id}"
    print(f"Test passed for test_id: {test_id}")
