from loose_change import loose_change


def test_caso_test():
    assert loose_change(29) == {'Nickels': 0,
                                'Pennies': 4, 'Dimes': 0, 'Quarters': 1}


def test_caso_test2():
    assert loose_change(91) == {'Nickels': 1,
                                'Pennies': 1, 'Dimes': 1, 'Quarters': 3}


def test_caso_test3():
    assert loose_change(0) == {'Nickels': 0,
                               'Pennies': 0, 'Dimes': 0, 'Quarters': 0}


def test_caso_test4():
    assert loose_change(-2) == {'Nickels': 0,
                                'Pennies': 0, 'Dimes': 0, 'Quarters': 0}


def test_caso_test5():
    assert loose_change(3.9) == {'Nickels': 0,
                                 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
