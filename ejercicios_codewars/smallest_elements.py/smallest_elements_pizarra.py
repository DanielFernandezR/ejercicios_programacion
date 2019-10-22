def first_n_smallest(listaNumeros, elementosTotal):
    listaMinimos = []
    for numero in (listaNumeros):
        if numero not in listaMinimos:
            listaMinimos.append(numero)
        else:
            None
    return listaMinimos


if __name__ == "__main__":

    assert first_n_smallest([7, 5, 1, 7, 6], 4) == [7, 5, 1, 6]
    assert first_n_smallest([7, 5, 1, 7, 7], 4) == [7, 5, 1, 7]
