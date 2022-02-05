x = "Soy variable global"

def local():
    x = x = "Soy variable local"
    
    def funcion_dentro_funcion():
        x = x = "Soy variable dentro de una funcion que a su vez está dentro de otra funcion"
        print(x)

    funcion_dentro_funcion()

    print(x)

local()

print(x)