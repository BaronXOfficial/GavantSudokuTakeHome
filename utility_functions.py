from pathlib import Path
from exceptions import InputRowLengthException, InputColumnLengthException, SolutionFailedException


class Helpers:
    def get_puzzle(self, puzzle_name, directory='puzzles'):
        """
        Inputs:
            - puzzle_name: 'puzzle1.txt'
            - directory: 'puzzles'

        path_in = get_single_puzzle(puzzle_name, directory) -> pathlib Path object

        Outputs:
            - split_out: List of Strings read from file
                * Elements of split_out are the rows of the Sudoku puzzle to be solved
            - directory: 'puzzles'
        """
        path_in = self.get_single_puzzle(puzzle_name, directory)
        read_out = path_in.read_text()
        split_out = read_out.split('\n')
        return split_out, directory

    def get_single_puzzle(self, puzzle_name, directory='puzzles'):
        """
        Input:
            - puzzle_name: 'puzzle1.txt'
            - directory: 'puzzles'
        Output:
            - path_out: Path object of file
        """
        path_out = Path.cwd().joinpath(directory, puzzle_name)
        return path_out

    def clean_puzzle(self, puzzle_split):
        """
        Input:
            - puzzle_split: List of Strings(Rows)
        Output:
            - clean_out: List of Lists(Rows of Elements) with empty rows removed
        """
        clean_out = [list(row) for row in puzzle_split if row != '']
        return clean_out

    def check_basic_validity(self, puzzle):
        """
        Input:
            - puzzle: List of Lists(Rows of Elements)

        if number of rows (len(puzzle)) is not 9:
            raise Column Length Exception, msg: 'Solution Failed - Invalid Column Length!'
        if number of columns (len(row)) is not 9:
            raise Row Length Exception, msg: 'Solution Failed - Invalid Row Length in Row {Row #}

        if none of the above conditions are met, returns None and moves on
        """
        if len(puzzle) != 9:
            raise InputColumnLengthException(f'Solution Failed - Invalid Column Length!')
        for row_number, row in enumerate(puzzle):
            if len(row) != 9 and row != '':
                raise InputRowLengthException(f'Solution Failed - Invalid Row Length in Row {row_number}!')

    def sudoku_solver(self, puzzle):
        """
        Input:
            - puzzle: List of Lists(rows of elements)

        empty = find_empty(puzzle) -> Boolean
            if False:
                ** If False, this means no further empty spaces remain and the solution is complete **
                Return Puzzle Output
            else:
                Get # Row and # Column of first Empty square (row by row, column by column)

        for # 1-9:
            guess (1-9) -> str
            check_for_validity(puzzle, row_number, column_number, guess) -> Boolean
                if True:
                    Write guess to specified square
                    Re-Enter recursion loop with new Puzzle object
                if False:
                    Check next guess (1-9)
                if Recursion finishes and returns False, restore 'X' for the specified square, backtrack recursion one level
            if none of the (1-9) options are valid for the specified square, backtrack recursion to the previous square
        """
        empty = self.find_empty(puzzle)
        if not empty:
            return puzzle
        else:
            row_number, column_number = empty

        for i in range(1, 10):
            guess = str(i)
            if self.check_for_validity(puzzle, row_number, column_number, guess):
                puzzle[row_number][column_number] = guess

                if self.sudoku_solver(puzzle):
                    return puzzle

                puzzle[row_number][column_number] = 'X'
        return False

    def check_for_validity(self, puzzle, row_number, column_number, guess):
        """
        Input:
            - puzzle: List of Lists(Rows of Elements)
            - row_number: y coordinate of guess: int
            - column_number: x coordinate of guess: int
            - guess: string version of integer guess (1-9)
        If all validation checks return True:
            Return True
        """
        valid_row = self.check_for_row_validity(puzzle, row_number, guess)
        valid_column = self.check_for_column_validity(puzzle, row_number, column_number, guess)
        valid_box = self.check_for_box_validity(puzzle, row_number, column_number, guess)
        if valid_row and valid_column and valid_box:
            return True

    def check_for_row_validity(self, puzzle, row_number, guess):
        """
        Input:
            - puzzle: List of Lists(Rows of Elements)
            - row_number: y coordinate of guess
            - guess: string version of integer guess (1-9)
        for element in row:
            if guess already exists in row:
                Return False
            else:
                Return True
        """
        for index, value in enumerate(puzzle[row_number]):
            if puzzle[row_number][index] == guess:
                return False
        return True

    def check_for_column_validity(self, puzzle, row_number, column_number, guess):
        """
        Input:
            - puzzle: List of Lists(Rows of Elements)
            - row_number: y coordinate of guess
            - column_number: x coordinate of guess
            - guess: string version of integer guess (1-9)
        for row in puzzle:
            if value of index of row matches guess:
                return False
            else:
                return True
        """
        for index, value in enumerate(puzzle):
            if puzzle[index][column_number] == guess and row_number != index:
                return False
        return True

    def check_for_box_validity(self, puzzle, row_number, column_number, guess):
        """
        Input:
            - puzzle: List of Lists(Rows of Elements)
            - row_number: y coordinate of guess
            - column_number: x coordinate of guess
            - guess: string version of integer guess (1-9)

        for x coordinate of guess:
            floor division of coordinate by 3 (division with no remainder), then multiplied by 3:
                eg: coordinate = 4 // 3 = 1
                    base_x_value_box = 3
                Thus defining the x coordinate "anchor" of the square to be tested
        for y coordinate of guess:
            floor division of coordinate by 3, then multiplied by 3
                eg coordinate = 7 // 3 = 2
                    base_y_value_box = 6

        for range (coordinate ... coordinate+3):
            creates the bounding box for the 3*3 grid to be tested

        if guess is found within bounding box:
            Return False
        else:
            Return True
        """
        base_x_value_box = (column_number // 3)*3
        base_y_value_box = (row_number // 3)*3


        for i in range(base_y_value_box, base_y_value_box + 3):
            for j in range(base_x_value_box, base_x_value_box + 3):
                if puzzle[i][j] == guess and i != row_number and j != column_number:
                    return False
        return True

    def find_empty(self, puzzle):
        """
        Input:
            - puzzle: List of Lists(Rows of Elements)

        Iterate through elements in each row
        and Rows within Puzzle

        if an 'X' is found:
            return y,x coordinates of empty square
        else:
            return None
        """
        for row_num, row in enumerate(puzzle):
            for col_num, col in enumerate(puzzle[row_num]):
                if puzzle[row_num][col_num] == 'X':
                    return (row_num, col_num)
        return None

    def solution_failed(self, file_split):
        """Basic error handling function for Failed Solution Error"""
        raise SolutionFailedException(f'Solution Failed - Unable to find Solution for {file_split[0]}')

    def write_to_file(self, puzzle, puzzle_file, directory='puzzles'):
        """
        Input:
            - puzzle: List of Lists(Rows of Elements) or String (Error Response)
            - puzzle_file: Split name of input file eg. 'puzzle1'
            - directory: Directory of file

        If the type of input puzzle is String:
            * Write the error response to the solution file
        else:
            * Join the elements of each row into a string
            * Join each row into one unified string separated by new line characters
            * Write the output puzzle to the solution file
        """
        path_out = Path.cwd().joinpath(directory, f'{puzzle_file}.sln.txt')
        if type(puzzle) == str:
            Path(path_out).write_text(puzzle)
        else:
            write_out = [''.join(row) for row in puzzle]
            final_out = ''.join([''.join(f'{line}\n' for line in write_out)])
            Path(path_out).write_text(final_out)

    def get_all_files(self, directory='puzzles'):
        """
        Input:
            directory: Directory of files - eg. 'puzzles'

        Output:
            Return list of all path objects of type .txt within specified directory
        """
        all_files = []
        all_files.extend(Path(directory).glob('*.txt'))
        return all_files


