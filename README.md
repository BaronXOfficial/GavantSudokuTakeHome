"# GavantSudokuTakeHome" 

____________________________
Instructions for Use:
____________________________

Step 1:

Create virtual environment for execution

Step 3:

Run sudoku.py to execute default operations:

By default, the following operations will be run:

- puzzle1.txt will be solved
- all puzzles in 'test_puzzles' will be solved

Instructions/Descriptive Comments are lodged within all methods

____________________________

Primary use should be within sudoku.py,

SudokuPuzzle is instantiated as sudoku and its methods can be called:

methods: 
    -call_solve:
        - Takes a single sudoku file and returns an output
    -run_all_files:
        - Takes a directory and runs call_solve on all .txt files


utility_functions are primarily helpers but can also be invoked 
if properly called, instructions included in each

tests.py has a handful of test functions demonstrating the major
error/exception handling and successful response

exceptions.py has custom error handling

puzzles are by default read from the 'puzzles' directory but any can be created and specified

'test_puzzles' has a handful of both working and intentionally nonworking Sudoku boards

____________________________
Notes on submission:
____________________________

This was a very fun challenge indeed, I had some ideas for further improvements
to the algorithm but for the sake for a reasonably timely submission I felt this
was good enough as it is far better than a naive brute force solution.

I considered trying to make an intelligent loop which iterates through all elements
and fills spaces which have only 1 possible solution, followed by 2 and increasing 
backtracking if a solution is ever impossible.

It'd be interesting to attempt such a solution and compare the time to complete
as I suspect it'd be faster and more "human" in its approach albeit still
relatively complex timewise. The optimal solution, by my view,
would be a "human" approach where the algorithm has a metric for information density 
on the board and can make guesses based on the probability of a given input.

I think such a solution would be more difficult to implement and likely totally overkill but it'd
definitely also undoubtedly be an efficient algorithm if it were somehow managed.

I included descriptive and informative comments in each method detailing input/output as well as
an overview of basic functions in plain English phrasing such that another engineer 
could quickly and easily understand the basic methods/means of the solution.

Likewise, I wrote a handful of tests to demonstrate the working error handling and successful output.

I think additionally I'd also like to add a perftime metric so that I can better evaluate the
time efficiency of the algorithmic methods. 

All in all, I'm happy with the outcome, and I hope that you will be as well!

Thank you for the opportunity, looking forward to your feedback 
as I'm always looking for ways to learn and improve further as an engineer!

Keep the Fire Alive Inside You!

- Anthony