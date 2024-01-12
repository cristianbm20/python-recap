"""
Funcion que devuelve True si dentro de un string dado
hay 3 o más palabras consecutivas. False si por el 
contrario hay numeros que impiden que haya tres o más
palabras consecutivas.
"""


def checkio(words: str) -> bool:
    """
    input: words (str)
    output: True si hay 3 o más palabras consecutivas (bool)
    """
    lista = words.split()
    contador = []
    for i in lista:
        if i.isalpha():
            contador.append(i)
            if len(contador) >= 3:
                return True
        else:
            contador.clear()
    return False


print(checkio("doce meses 12 tiene un año"))  # True
print(checkio("12 meses tiene 1 año"))  # False
