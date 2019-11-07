def wave(str):
    resultado = []
    for posicion, letra in enumerate(str[:]):
        if letra == " ":
            None
        else:
            mayuscula = str[posicion].upper()
            palabraCompleta = str[:posicion] + mayuscula + str[posicion + 1:]
            resultado.append(palabraCompleta)
    return resultado


if __name__ == "__main__":

    assert wave("codewars") == ["Codewars", "cOdewars", "coDewars",
                                "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
    assert wave("two words") == ["Two words", "tWo words", "twO words",
                                 "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
    assert wave(" gap ") == [" Gap ", " gAp ", " gaP "]
