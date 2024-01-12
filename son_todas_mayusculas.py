"""
Programa que devuelve true o false en funcion de si todas las letras de un 
string dado son mayusculas. En caso de estar vacio o no tener ninguna letra 
devolverá true.

def son_todas_mayus(string):
    if not string or string.isspace() or any(chr.isdigit() for chr in string):
        return True
    return string.isupper()

print(son_todas_mayus("SALUDOS VIAJEROS"))
"""

# Forma más sencilla.


def son_todas_mayus(string):
    """
    input: string (str)
    output: True or False (bool)
    """
    return string.upper() == string


print(son_todas_mayus("1234"))
