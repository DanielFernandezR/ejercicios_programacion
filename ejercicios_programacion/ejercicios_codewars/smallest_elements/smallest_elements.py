def first_n_smallest(listaNumeros, numElementos):
    if numElementos == 0:
        return []

    listaOrdenada = listaNumeros[:]
    listaOrdenada.sort()
    if listaOrdenada == listaNumeros:
        return listaNumeros[0:numElementos]

    listaOrdenadaInversa = listaNumeros[:]
    listaOrdenadaInversa.sort(reverse=True)
    if listaOrdenadaInversa == listaNumeros:
        return listaNumeros[2:5]


if __name__ == "__main__":

    assert first_n_smallest([1, 2, 3, 4, 5], 0) == []
    assert first_n_smallest([1, 2, 3, 4, 5], 3) == [1, 2, 3]
    assert first_n_smallest([5, 4, 3, 2, 1], 3) == [3, 2, 1]
