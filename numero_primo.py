"""
Programa que comprueba si el numero pasado es primo. 
"""


def es_primo(numero):
    """
    input: numero (int)
    output: True si es primo, False si no lo es (bool)
    """
    assert numero > 0
    contador = 2
    while contador < numero:
        if numero % contador == 0:
            return False
        contador += 1
    return True


NUM = 3
print(es_primo(NUM))
