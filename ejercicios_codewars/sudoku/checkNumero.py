def checkNumeros(sudoku):
    assert isinstance(sudoku, list)
    for lista in sudoku:
        for caracter in lista:
            if caracter != str(int):
                return False
    return True


if __name__ == "__main__":
    assert checkNumeros([[1, 2, 3],
                         [2, 3, 1],
                         [3, 1, 2]])
    assert checkNumeros([['a', 'b', 'c'],
                         ['b', 'c', 'a'],
                         ['c', 'a', 'b']])
