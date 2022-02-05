from datetime import datetime 


def decoradora(funct):
    def envoltura():
        print("Esto se añade a mi funcion original")
        funct()
    return envoltura

def saludar():
    print("Hola")

print("Funcion Sola:")
saludar()

#Forma normal
print("Funcion a la antigua:")
saludar = decoradora(saludar)
saludar()

#forma Sugar Sintax
print("Funcion Decorada:")
@decoradora
def saludar2():
    print("2. Hola")

saludar2()


def uppers(funcion):
    def envolver(frase):
        return funcion(frase).upper()
    return envolver

@uppers
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

7568
@execution_time
def random_timer():
    for _ in range(1, 1000000):
        pass

@execution_time
def suma (a: int, b: int) -> int:
    return a + b


def run():
    print(mensaje("Fernando"))
    random_timer()
    suma(125345855564333666, 5556433587156055456)


if __name__ == '__main__':
    run()