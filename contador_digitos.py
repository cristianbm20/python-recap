"""
Funcion que cuenta los digitos que aparecen en un 
string pasado como argumento
"""


def count_digits(text: str) -> int:
    """
    input: text (str)
    output: numero de digitos en text (int)
    """
    contador = 0
    for i in text:
        if i.isdigit():
            contador += 1
    return contador


print(count_digits('H0la com0 3stam0s'))
