def checkFilas(sudoku):
    assert isinstance(sudoku, list)

    for fila in sudoku:
        for (posicion, numero) in enumerate(fila):
            if numero in fila[posicion + 1:]:
                return False
                break
    return True
    assert isinstance(checkFilas, bool)


if __name__ == "__main__":
    assert checkFilas([[1, 2, 3],
                       [2, 3, 1],
                       [3, 1, 2]])
