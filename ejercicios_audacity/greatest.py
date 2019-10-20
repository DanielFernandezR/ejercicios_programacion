# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.


def greatest(lista):
    bigger = 0
    for numero in lista:
        if bigger < numero:
            bigger = numero
        else:
            None
    return bigger


print(greatest([4, 23, 1]))
# >>> 23
print(greatest([]))
# >>> 0
print(greatest([1, -12, 45, 20]))
# >>> 45
