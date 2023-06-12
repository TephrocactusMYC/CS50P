import pytest
from project import generate_sudoku,read_sudoku,solve_sudoku,save_sudoku
def test_generate_sudoku():
    # 生成的数独问题应为9x9的二维数组
    sudoku_matrix = generate_sudoku()
    assert len(sudoku_matrix) == 9
    assert len(sudoku_matrix[0]) == 9

def test_read_sudoku():
    # 读取到的数独问题应与文件中的内容一致
    filepath = 'sudoku.txt'
    sudoku_matrix = generate_sudoku()
    save_sudoku(filepath, sudoku_matrix)
    read_sudoku_matrix = read_sudoku(filepath)
    assert read_sudoku_matrix == sudoku_matrix

def test_solve_sudoku():
    # 解出的数独问题应为9x9的二维数组，每行列均有1~9的数字，且3x3子块中也均有1~9的数字
    filepath = 'sudoku.txt'
    sudoku_matrix = generate_sudoku()
    save_sudoku(filepath, sudoku_matrix)
    solved_sudoku_matrix = solve_sudoku(sudoku_matrix)
    assert len(solved_sudoku_matrix) == 9
    for i in range(9):
        assert sorted(solved_sudoku_matrix[i]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert sorted([solved_sudoku_matrix[j][i] for j in range(9)]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            sub_block = []
            for i in range(3):
                for j in range(3):
                    sub_block.append(solved_sudoku_matrix[x + i][y + j])
            assert sorted(sub_block) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
