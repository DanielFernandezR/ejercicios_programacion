import time
from duplicate_encoder_diccionario import duplicate_encode as diccionarios
from duplicate_encoder import duplicate_encode as strings


def benchmark(func, *args):
    start_time = time.clock()
    func(*args)
    run_time = time.clock() - start_time
    return run_time


if __name__ == "__main__":

    print("\n### Caso test largo ###\n")
    print("diccionarios => " +
          str(benchmark(diccionarios, ('Maria es mUy buena chic@!!'))))
    print("diccionarios => " +
          str(benchmark(strings, ('Maria es mUy buena chic@!!'))))

    print("\n### Caso test AbrirCerrarCaracteres ###\n")
    print("diccionarios => " + str(benchmark(diccionarios, ('recede'))))
    print("strings => " + str(benchmark(strings, ('recede'))))

    print("\n### Caso test ConMayusculas  ###\n")
    print("diccionarios => " + str(benchmark(diccionarios, ('Success'))))
    print("strings => " + str(benchmark(strings, ('Success'))))
