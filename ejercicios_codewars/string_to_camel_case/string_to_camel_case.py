def to_camel_case(text):
    resultado = text
    if text == "":
        return text
    else:
        resultado = resultado.replace("_", "")
        resultado = resultado.replace("-", "")
        return resultado


if __name__ == "__main__":

    assert to_camel_case('') == ''
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
