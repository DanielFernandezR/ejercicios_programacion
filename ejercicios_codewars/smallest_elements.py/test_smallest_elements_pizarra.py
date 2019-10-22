from smallest_elements_pizarra import first_n_smallest


def test_devolver_elementos_no_repetidos():
    assert first_n_smallest([7, 5, 1, 7, 6], 4) == [7, 5, 1, 6]
