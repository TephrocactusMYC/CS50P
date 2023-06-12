# SUDOKU GAME
#### Video Demo:  [LINK]
#### Description:
##### What
This is a sudoku game application that mainly deals with generating, reading and solving Sudoku puzzles. The solution will be printed on the console.

Specifically, its main features are:
- Generate Sudoku puzzles: The program is capable of generating valid 9x9 Sudoku puzzles, where each row, column and 3x3 sub-block contains the digits 1 through 9 exactly once.
- Solve Sudoku puzzles: The program is capable of solving a given Sudoku puzzle using a backtracking algorithm.

Using this program, one can easily generate and solve Sudoku puzzles, as well as use their own input files to validate and solve Sudoku puzzles. The program also uses pytest to test the correctness of its features, ensuring the functionality of generating Sudoku puzzles, reading Sudoku puzzles and solving Sudoku puzzles.
##### Why
This is my final project for CS50P. For god sake, everybody sould try to do some sudoku puzzles.

##### Status
This is not being actively developed, though there are certainly
improvements that could be made. This is just a toy program for Sudoku, and the solution cannot guarantee uniqueness. What's more, the speed of the program is not pretty. Some small bug may exist etc..


##### How do I use it?
```bash
python project.py
# test for it
pytest test_project.py
```

##### Example
###### Puzzle
<table><tr><td>0</td><td>0</td><td>6</td><td>0</td><td>1</td><td>0</td><td>8</td><td>7</td><td>0</td></tr><tr><td>8</td><td>1</td><td>3</td><td>0</td><td>0</td><td>7</td><td>2</td><td>0</td><td>6</td></tr><tr><td>0</td><td>9</td><td>4</td><td>0</td><td>0</td><td>2</td><td>1</td><td>3</td><td>0</td></tr><tr><td>9</td><td>0</td><td>0</td><td>4</td><td>3</td><td>8</td><td>0</td><td>2</td><td>1</td></tr><tr><td>4</td><td>3</td><td>1</td><td>2</td><td>7</td><td>6</td><td>0</td><td>0</td><td>8</td></tr><tr><td>0</td><td>0</td><td>8</td><td>1</td><td>5</td><td>0</td><td>7</td><td>0</td><td>0</td></tr><tr><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>3</td><td>6</td><td>2</td></tr><tr><td>3</td><td>8</td><td>0</td><td>6</td><td>9</td><td>4</td><td>5</td><td>1</td><td>7</td></tr><tr><td>1</td><td>6</td><td>7</td><td>0</td><td>2</td><td>5</td><td>4</td><td>0</td><td>9</td></tr></table>

###### Solution
<table><tr><td>2</td><td>5</td><td>6</td><td>9</td><td>1</td><td>3</td><td>8</td><td>7</td><td>4</td></tr><tr><td>8</td><td>1</td><td>3</td><td>5</td><td>4</td><td>7</td><td>2</td><td>9</td><td>6</td></tr><tr><td>7</td><td>9</td><td>4</td><td>8</td><td>6</td><td>2</td><td>1</td><td>3</td><td>5</td></tr><tr><td>9</td><td>7</td><td>5</td><td>4</td><td>3</td><td>8</td><td>6</td><td>2</td><td>1</td></tr><tr><td>4</td><td>3</td><td>1</td><td>2</td><td>7</td><td>6</td><td>9</td><td>5</td><td>8</td></tr><tr><td>6</td><td>2</td><td>8</td><td>1</td><td>5</td><td>9</td><td>7</td><td>4</td><td>3</td></tr><tr><td>5</td><td>4</td><td>9</td><td>7</td><td>8</td><td>1</td><td>3</td><td>6</td><td>2</td></tr><tr><td>3</td><td>8</td><td>2</td><td>6</td><td>9</td><td>4</td><td>5</td><td>1</td><td>7</td></tr><tr><td>1</td><td>6</td><td>7</td><td>3</td><td>2</td><td>5</td><td>4</td><td>8</td><td>9</td></tr></table>


