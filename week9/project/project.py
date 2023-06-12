import random

# generate sudoku puzzle
def generate_sudoku():
    sudoku = [[0 for i in range(9)] for j in range(9)]
    pattern = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                random.shuffle(pattern)
                for k in pattern:
                    if k not in sudoku[i] and k not in [sudoku[x][j] for x in range(9)] and k not in [sudoku[x][y] for x in range((i // 3) * 3, (i // 3 + 1) * 3) for y in range((j // 3) * 3, (j // 3 + 1) * 3)]:
                        sudoku[i][j] = k
                        break
                else:
                    return generate_sudoku()  # retry


    blank_num = random.randint(30, 40)
    for i in range(blank_num):
        random_x = random.randint(0, 8)
        random_y = random.randint(0, 8)
        sudoku[random_x][random_y] = 0
    return sudoku


# read from txt
def read_sudoku(filepath):
    with open(filepath, 'r') as f:
        sudoku = []
        for line in f.readlines():
            row = list(map(int, line.strip().split()))
            sudoku.append(row)
        return sudoku


# print the solution
def print_sudoku(sudoku):
    for row in sudoku:
        print(' '.join(str(x) for x in row))


# solve sudoku puzzle
def solve_sudoku(sudoku):
    def check(x, y, k):
        for i in range(9):
            if sudoku[x][i] == k or sudoku[i][y] == k or sudoku[(x // 3) * 3 + i // 3][(y // 3) * 3 + i % 3] == k:
                return False
        return True

    def backtrack(index=0):
        if index == blank_indexes_len:
            return True
        x, y = blank_indexes[index]
        for k in range(1, 10):
            if check(x, y, k):
                sudoku[x][y] = k
                if backtrack(index + 1):
                    return True
                sudoku[x][y] = 0
        return False

    blank_indexes = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
    blank_indexes_len = len(blank_indexes)
    backtrack()
    return sudoku

# save answer
def save_sudoku(filepath, sudoku):
    with open(filepath, 'w') as f:
        for row in sudoku:
            f.write(' '.join(str(x) for x in row))
            f.write('\n')

# main
if __name__ == '__main__':
    generate_filepath = 'new_sudoku.txt'
    solve_filepath = 'sudoku.txt'

    sudoku = read_sudoku(solve_filepath)
    print('The solution: ')
    solved_sudoku = solve_sudoku(sudoku)

    sudoku = generate_sudoku()
    save_sudoku(generate_filepath, sudoku)

    print_sudoku(solved_sudoku)
    print('Also generate a new sudoku.')
