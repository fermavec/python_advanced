# Existen varios tipos de Typing en los lenguajes de 
# Programacion: Estatico y Dinamico que vab desde debil
# a fuerte. Python es Dinamico-Fuerte.
#Convirtiendo Python a tipado Estatico
from typing import Dict, List, Tuple
#Instale el modulo mypy con pip install en un entorno virtual

def run():
    suma(5, 12)
    setting()
    typing_dict_list()


def typing_dict_list():
    possitives: List[int] = [1, 2, 3, 4, 5]
    
    users: Dict[str, int] = {
        "Fernando": 2,
        "Patricia": 5,
        "Benji": 10
    }

    activities: List[Dict[str, str]] = [
        {
            "Usuario": "Fernando",
            "Actividad": "Correr"
        },
        {
            "Usuario": "Patricia",
            "Actividad": "Caminar"
        },
        {
            "Usuario": "Benji",
            "Actividad": "Saltar"
        }
    ]

    tuplas: Tuple [int, float, int] = (1, 1.05, 2)

    print(tuplas, activities, users, possitives)


def suma(d: int, e: int ) -> int:
    f = d + e
    print(f)
    

def setting():
    a: int = 5
    print(a)

    b: str = "Hola"
    print(b)

    c: bool = True
    print(c)


if __name__ == '__main__':
    run()