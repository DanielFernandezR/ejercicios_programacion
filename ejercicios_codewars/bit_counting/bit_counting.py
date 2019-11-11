def countBits(num):
    numeroBinario = bin(num)
    repeticiones = numeroBinario.count("1")
    return int(repeticiones)


if __name__ == "__main__":

    assert countBits(0) == 0
    assert countBits(4) == 1
    assert countBits(7) == 3
    assert countBits(9) == 2
    assert countBits(10) == 2
