def to_camel_case(frase):
    lista_frase = frase.replace('-', '_').split('_')
    resultado = [lista_frase[0]]
    for palabra in lista_frase[1:]:
        resultado.append(palabra.capitalize())
    return ''.join(resultado)


if __name__ == "__main__":

    assert to_camel_case('') == ''
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"
