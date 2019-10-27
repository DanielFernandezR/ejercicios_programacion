def comp(array1, array2):
    lista = []
    for numero in array1:
        if numero * numero in array2:
            lista.append(numero)
    if lista == array1:
        return True
    else:
        return False
