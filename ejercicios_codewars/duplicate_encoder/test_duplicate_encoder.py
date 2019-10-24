from duplicate_encoder_diccionario import duplicate_encode


def test_ninguno_se_repite():
    assert duplicate_encode("din") == "((("


def test_algunos_caracteres_repetidos(): 
    assert duplicate_encode("recede") == "()()()"


def test_caracter_en_mayuscula():
    assert duplicate_encode("Success") == ")())())"


def test_caracteres_especiales():
    assert duplicate_encode("(( @") == "))(("
