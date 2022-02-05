#Important!
#Correr con mypy nombredearchivo.py --check-untyped-defs

def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]


def run():
    print(is_palindrome("Anita lava la tina"))
    print(is_palindrome("Fernando"))
    print(is_palindrome(1000))


if __name__ == '__main__':
    run()