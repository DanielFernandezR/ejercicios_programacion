def loose_change(cents):
    numero = cents
    diccionario = {"Nickels": 0, "Pennies": 0, "Dimes": 0, "Quarters": 0}
    while numero >= 25:
        diccionario["Quarters"] = diccionario["Quarters"] + 1
        numero = numero - 25
    while numero >= 10:
        diccionario["Dimes"] = diccionario["Dimes"] + 1
        numero = numero - 10
    while numero >= 5:
        diccionario["Nickels"] = diccionario["Nickels"] + 1
        numero = numero - 5
    while numero >= 1:
        diccionario["Pennies"] = diccionario["Pennies"] + 1
        numero = numero - 1

    return diccionario


if __name__ == "__main__":

    assert(loose_change(29) == {'Nickels': 0,
                                'Pennies': 4, 'Dimes': 0, 'Quarters': 1})
    assert(loose_change(91) == {'Nickels': 1,
                                'Pennies': 1, 'Dimes': 1, 'Quarters': 3})
    assert(loose_change(0) == {'Nickels': 0,
                               'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
    assert(loose_change(-2) == {'Nickels': 0,
                                'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
    assert(loose_change(3.9) == {'Nickels': 0,
                                 'Pennies': 3, 'Dimes': 0, 'Quarters': 0})
