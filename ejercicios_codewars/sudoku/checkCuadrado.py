def checkCuadrado(sudoku):
    assert isinstance(sudoku, list)
    for lista in sudoku:
        if len(sudoku) != len(lista):
            return False
    return True


if __name__ == "__main__":
    assert checkCuadrado([[1, 2, 3],
                          [2, 3, 1],
                          [3, 1, 2]])
    assert checkCuadrado([[1, 2, 3],
                          [2, 3, 1],
                          [3, 1, 2, 5]])
