def make_division_by(n):

    def divisor(m):
        assert type(m) == int, "Debes ingresar un valor entero"
        return m / n
    
    return divisor


def make_repeater(n):

    def repeater(string):
        assert type(string) == str, "Solo se puede ingresar cadenas de texto"
        return string * n
    
    return repeater


def clousure(x):

    def anidada(n):
        return x * n 
    
    return anidada


def run():
    multiplicador_x_10 = clousure(10)
    multiplicador_x_5 = clousure(5)

    print(multiplicador_x_10(8))
    print(multiplicador_x_5(8))
    print(multiplicador_x_5(multiplicador_x_10(8)))

    repeat_4_times = make_repeater(4)

    print(repeat_4_times("Black "))
    print("Number ooooooooooonnnnnnneeeeeee")
    #print(repeat_4_times(10))

    challenge_by_3 = make_division_by(3)

    print(challenge_by_3(3233))
    #print(challenge_by_3(3.5))
    

if __name__ == '__main__':
    run()
