from square_root import raizEcuacionSegundoGrado


def test_raiz_nula_unica():
    assert raizEcuacionSegundoGrado(1, 0, 0) == 0


def test_coeficiente_c_nulo():
    x, y = raizEcuacionSegundoGrado(1, 1, 0)
    assert x == 0
    assert y == -1
