import random

def hogwarts(func):
    def wrapper(name):
        func(name)
        houses = ("Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw")
        selected_house = random.choice(houses)
        print("Hola "+ name + ", soy el sombrero seleccionador.")
        print("Tu hogar en Hogwarts será " + selected_house)
    return wrapper


@hogwarts
def the_hat(magician):
    print("Bienvenido " + magician)
    print("Ponte el sombrero seleccionador")
    input("Presiona enter cuando estes listo/a...")


def run():
    name = input("Ingresa tu nombre: ")
    the_hat(name)


if __name__ == '__main__':
    run()