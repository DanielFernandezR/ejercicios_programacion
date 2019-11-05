def checkNumerosEnteros(sudoku):
    assert isinstance(sudoku, list)
    sudokuSano = True
    for fila in sudoku:
        for numero in fila:
            if not isinstance(numero, int):
                sudokuSano = False
                break
    assert isinstance(sudokuSano, bool)
    return sudokuSano


def checkNumerosEnRango(sudoku):
    assert isinstance(sudoku, list)
    sudokuSano = True
    numeroValidos = range(1, len(sudoku) + 1)

    for fila in sudoku:
        for numero in fila:
            if numero not in numeroValidos:
                sudokuSano = False
                break
    assert isinstance(sudokuSano, bool)
    return sudokuSano


def checkNumeroValidos(sudoku):
    return checkNumerosEnRango(sudoku) and checkNumerosEnteros(sudoku)


if __name__ == "__main__":
    assert checkNumerosEnteros([[1, 2, 3],
                                [2, 3, 1],
                                [3, 1, 2]])
    assert checkNumerosEnRango([[1, 2, 3],
                                [2, 3, 1],
                                [3, 1, 2]])
    assert checkNumerosEnRango([[1, 2, 3],
                                [2, 4, 1],
                                [3, 1, 2]])
    assert checkNumerosEnteros([['a', 'b', 'c'],
                                ['b', 'c', 'a'],
                                ['c', 'a', 'b']])
