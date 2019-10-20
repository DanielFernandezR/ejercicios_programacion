spy = [0, 0, 7]
agent = spy
print(agent, spy)
spy[2] = agent[2] + 1
print(agent, spy)
# Aqui decimos que agent es lo mismo que spy,
# despues decimos que la 2º posicion de spy, que es 7
# que será lo mismo que 2º posicion de agente, + 1
# y al hacer print vemos que ha cambiado el 7 por 8 en ambas variables.
