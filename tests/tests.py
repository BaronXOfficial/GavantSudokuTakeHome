import unittest
from utility_functions import Helpers
from sudoku import SudokuPuzzle

helper = Helpers()
sudoku = SudokuPuzzle()


class SudokuTest(unittest.TestCase):
    def test_invalid_column_count_failure(self):
        """Test Invalid Column Count Exception
        Input is a .txt file with too many characters in line 1

        Expected return: Solution Failed - Invalid Row Length error
        """
        test_file = 'puzzle45.txt'
        directory = 'test_puzzles'
        expected_error = 'Solution Failed - Invalid Row Length in Row 0!'
        sudoku.call_solve(test_file, directory)
        self.assertEqual(expected_error, sudoku.call_solve(test_file, directory))

    def test_invalid_row_count_failure(self):
        """Test Invalid Row Count Exception
        Input is a .txt file with too many lines provided

        Expected return: Solution Failed - Invalid Column Length error
        """
        test_file = 'puzzle88.txt'
        directory = 'test_puzzles'
        expected_error = 'Solution Failed - Invalid Column Length!'

        self.assertEqual(expected_error, sudoku.call_solve(test_file, directory))


    def test_no_solution_failure(self):
        """Test No Solution Found Exception
        Input is a .txt file Sudoku with no possible solution

        Expected return: Solution Failed - Unable to find Solution error
        """
        test_file = 'puzzle6.txt'
        directory = 'test_puzzles'
        expected_error = 'Solution Failed - Unable to find Solution for puzzle6'

        self.assertEqual(expected_error, sudoku.call_solve(test_file, directory))

    def test_file_not_found_failure(self):
        """Test File Not Found Exception
        Input is a .txt string to a non-existent file

        Expected return: 'Error! File not found in specified directory!'
        """
        test_file = "fakefile.txt"
        directory = 'test_puzzles'
        expected_error = 'Error! File not found in specified directory!'

        self.assertEqual(expected_error, sudoku.call_solve(test_file, directory))

    def test_working_solution_success(self):
        test_file = 'puzzle1.txt'
        directory = 'test_puzzles'
        expected_output = [
            ['4', '2', '8', '1', '5', '9', '6', '7', '3'],
            ['1', '9', '6', '3', '7', '4', '8', '2', '5'],
            ['3', '7', '5', '8', '6', '2', '9', '4', '1'],
            ['9', '8', '1', '4', '2', '3', '5', '6', '7'],
            ['5', '6', '4', '7', '1', '8', '3', '9', '2'],
            ['7', '3', '2', '5', '9', '6', '1', '8', '4'],
            ['2', '4', '3', '6', '8', '1', '7', '5', '9'],
            ['6', '1', '7', '9', '4', '5', '2', '3', '8'],
            ['8', '5', '9', '2', '3', '7', '4', '1', '6']]

        self.assertEqual(expected_output, sudoku.call_solve(test_file, directory))

