def first_n_smallest(listaNumeros, elementosTotal):
    listaOrdenada = sorted(listaNumeros)[:elementosTotal]
    resultado = []
    for num in listaNumeros:
        if num in listaOrdenada:
            resultado.append(num)
            listaOrdenada.remove(num)
        if len(resultado) == elementosTotal:
            return resultado


if __name__ == "__main__":
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 2) == [2, 1]
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 3) == [2, 1, 2]
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 4) == [2, 1, 2, 2]