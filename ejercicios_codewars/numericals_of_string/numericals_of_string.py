def numericals(frase):
    contarValores = {}
    resultado = ""
    for caracter in frase:
        contarValores[caracter] = contarValores.get(caracter, 0) + 1
        resultado += str(contarValores[caracter])
    return resultado


if __name__ == "__main__":

    assert numericals("Hello, World!") == "1112111121311"
    assert numericals("Hello, World! It's me, JomoPipi!") == "11121111213112111131224132411122"
    assert numericals("hello hello") == "11121122342"
    assert numericals("Hello") == "11121"
    assert numericals("aaaaaaaaaaaa") == "123456789101112"
