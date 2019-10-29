def loose_change(cambio):
    nombre_monedas = ["Quarters", "Dimes", "Nickels", "Pennies"]
    valores_monedas = [25, 10, 5, 1]
    cartera = dict(zip(nombre_monedas, valores_monedas))
    numero_monedas = []

    if cambio <= 0:
        return {"Nickels": 0, "Pennies": 0, "Dimes": 0, "Quarters": 0}
    else:
        for moneda in reversed(sorted(list(cartera.values()))):
            uso_monedas = 0
            while cambio >= moneda:
                cambio -= moneda
                uso_monedas += 1
            numero_monedas.append(uso_monedas)
            
    cartera = dict(zip(nombre_monedas, numero_monedas))
    return cartera
