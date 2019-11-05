def checkColumnas(sudoku):
    assert isinstance(sudoku, list)
    numeroFilas = len(sudoku)
    indexFilaActual = 0
    
    for fila in sudoku:
        for numero in fila:
            indexFilaSiguiente = indexFilaActual + 1

            while indexFilaSiguiente < numeroFilas:
                try:
                    posicionNumeroFilasSiguiente = sudoku[indexFilaSiguiente].index(numero)
                except ValueError:
                    return False
                else:
                    if posicionNumeroFilasSiguiente == fila.index(numero):
                        return False
                    else:
                        indexFilaSiguiente += 1
        indexFilaActual += 1
    return True


if __name__ == "__main__":
    assert checkColumnas([[1, 2, 3],
                       [2, 3, 1],
                       [3, 1, 2]])