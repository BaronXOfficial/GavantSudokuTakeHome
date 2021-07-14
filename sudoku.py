import copy
from utility_functions import Helpers
from exceptions import InputRowLengthException, InputColumnLengthException, SolutionFailedException



helper = Helpers()




class SudokuPuzzle:
    def call_solve(self, puzzle_file: str, directory='puzzles'):
        """
        Input:
            - Filename of file - eg: 'puzzle1.txt'
            - Directory for file - eg: 'puzzles'

        Output:
            - Error written to file and Returned if encountered:
                * Invalid # of Rows
                * Invalid # of Columns
                * Unable to reach Solution
            - Generic Error Handling:
                * File not found
                * Base Exception with Error readout
            - Successfully Completed Puzzle written to file and Returned
        """
        try:
            file_split = puzzle_file.split('.')
            split_out, directory = helper.get_puzzle(puzzle_file, directory)
            clean_out_original = helper.clean_puzzle(split_out)
            helper.check_basic_validity(clean_out_original)
            clean_out_input = copy.deepcopy(clean_out_original)
            solver = helper.sudoku_solver(clean_out_input)
            if solver:
                helper.write_to_file(solver, file_split[0], directory)
                print(f'{puzzle_file} in {directory} complete!')
                return solver
            else:
                helper.solution_failed(file_split)
                solution_failed = 'Solution Failed - Unable to find Solution!'
                print(solution_failed)
                helper.write_to_file(solution_failed, file_split[0], directory)

        except InputColumnLengthException as invalidColumnLengthError:
            print(invalidColumnLengthError.msg)
            helper.write_to_file(invalidColumnLengthError.msg, file_split[0], directory)
            return invalidColumnLengthError.msg
        except InputRowLengthException as invalidRowLengthError:
            print(invalidRowLengthError.msg)
            helper.write_to_file(invalidRowLengthError.msg, file_split[0], directory)
            return invalidRowLengthError.msg
        except SolutionFailedException as solutionFailedError:
            print(solutionFailedError.msg)
            helper.write_to_file(solutionFailedError.msg, file_split[0], directory)
            return solutionFailedError.msg
        except FileNotFoundError:
            file_error = 'Error! File not found in specified directory!'
            print(file_error)
            return file_error
        except BaseException as e:
            base_error = f"An unexpected error has occured. If it persists please contact the administrator. Error: {e}"
            print(base_error)
            return(base_error)

    def run_all_files(self, directory='puzzles'):
        """
        Input: Directory

        Iterates through every file ending in '.txt' in directory
        Excludes files ending in '.sln.txt' as those are considered already complete
        Runs solving algorithm for every file within directory
        Prints a "complete" message with every item completed


        """
        all_files = helper.get_all_files(directory)
        for file in all_files:
            if not file.name.endswith('.sln.txt'):
                self.call_solve(file.name, directory)






sudoku = SudokuPuzzle()

if __name__ == '__main__':
    sudoku.call_solve('puzzle1.txt', 'puzzles')
    sudoku.run_all_files('test_puzzles')