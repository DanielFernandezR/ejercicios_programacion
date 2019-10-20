def sum(a, b):
    a = a + b
    return a


s = 'Hello '
t = 'Dave!'

print(sum(2, 115))
print(sum(s, t))


def abbaize(PrimeraString, SegundaString):
    return PrimeraString + SegundaString + SegundaString + PrimeraString


print(abbaize('a', 'b'))
print(abbaize('dog', 'cat'))


def find_second(FirstString, SecondString):
    first_find_string = FirstString.find(SecondString)
    second_find_string = FirstString.find(SecondString, first_find_string + 1)
    return second_find_string


danton = "De l'audace, encore de l'audace, toujours de l'audace"
print(find_second(danton, 'audace'))
# >>> 25

twister = "she sells seashells by the seashore"
print(find_second(twister, 'she'))
# >>> 13
