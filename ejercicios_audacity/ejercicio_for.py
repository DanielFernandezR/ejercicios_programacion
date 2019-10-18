def measure_udacity(primera_letra_U):
    result = 0
    for i in primera_letra_U:
        if i[0] == "U":
            result = result + 1
    return result


print(measure_udacity(['Dave', 'Sebastian', 'Katy']))

print(measure_udacity(['umika', 'Umberto']))
