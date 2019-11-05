from checkCuadrado import checkCuadrado
from checkNumero import checkNumeroValidos
from checkFilas import checkFilas
from checkColumnas import checkColumnas


def checkSudoku(sudoku):
    return checkCuadrado(sudoku) and checkNumeroValidos(sudoku) \
        and checkFilas(sudoku) and checkColumnas(sudoku)


if __name__ == '__main__':

    import casosTestSudoku

    for attr in sorted(casosTestSudoku.__dict__):
        # Scan namespace keys (or enumerate) del objeto modulo checkCuadrado
        # Asi podemos añadir todos los casos que queramos
        # en la unidad cassTestSudoku sin modificar este codigo
        if attr.startswith('__'):
            pass
            # Skip atributo
        else:
            print(attr, " => ", checkSudoku(casosTestSudoku.__dict__[attr]))
            # mismo codigo que getattr(module, attr)
            # es necesario añadir el espacio de nombres del modulo:
            # casosTestSudoku.irregular
