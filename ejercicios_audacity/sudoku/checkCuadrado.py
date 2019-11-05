def checkCuadrado(sudoku):
    assert isinstance(sudoku, list)
    sudokuSano = True

    for lista in sudoku:
        if len(sudoku) != len(lista):
            sudokuSano = False
            break

    assert isinstance(sudokuSano, bool)
    return sudokuSano


if __name__ == "__main__":
    assert checkCuadrado([[1, 2, 3],
                          [2, 3, 1],
                          [3, 1, 2]])
    assert checkCuadrado([[1, 2, 3],
                          [2, 3, 1],
                          [3, 1, 2, 5]])
