"""
Funcion que elimina los acentos de un string. 
"""

from unicodedata import normalize, category


def checkio(in_string):
    """
    input: string con acentos (str)
    output: string sin acentos (str)
    """
    return ''.join(x for x in normalize('NFD', in_string) if category(x) != 'Mn')


print(checkio("camión, pingüino y Logroño "))
print(checkio("loài trăn lớn"))
print(checkio("蟒蛇"))
