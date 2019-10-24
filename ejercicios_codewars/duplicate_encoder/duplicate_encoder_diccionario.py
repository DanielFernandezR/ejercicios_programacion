def duplicate_encode(word):
    diccionario = {}
    for caracter in word:
        word = word.lower()
        if caracter in diccionario:
            diccionario[caracter] = ")"
        else:
            diccionario[caracter] = "("
    assert diccionario != {}
    palabraCodificada = ""
    for caracter in word:
        palabraCodificada = palabraCodificada + diccionario[caracter]
    return palabraCodificada
