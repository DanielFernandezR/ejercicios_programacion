def growing_plant(upSpeed, downSpeed, desiredHeight):
    if upSpeed <= desiredHeight or upSpeed >= desiredHeight:
        pesoAhora = 0
        dias = 0
        while pesoAhora <= desiredHeight:
            pesoAhora = pesoAhora + upSpeed
            dias = dias + 1
            if pesoAhora >= desiredHeight:
                return dias
            else:
                pesoAhora = pesoAhora - downSpeed


if __name__ == "__main__":

    assert growing_plant(100, 10, 910) == 10
    assert growing_plant(10, 9, 4) == 1
    assert growing_plant(5, 2, 0) == 1
    assert growing_plant(5, 2, 5) == 1
    assert growing_plant(5, 2, 6) == 2
