# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.


def product_list(listaNum):
    resultado = 1
    for numero in listaNum:
        resultado = resultado * numero
    return resultado


print(product_list([9]))
# >>> 9

print(product_list([3, 2, 3, 4]))
# >>> 72

print(product_list([]))
# >>> 1
