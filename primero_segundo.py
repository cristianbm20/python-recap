"""
Funcion que devuelva True o False en funcion de si los parametros
first y second coinciden con la palabra word.
"""


def goes_after(word: str, first: str, second: str) -> bool:
    """
    input: word (str), first (str), second (str)
    output: True or False (bool)
    """
    if first in word and second in word:
        indice = word.index(first)
        if word.index(second) == indice + 1:
            return True
        return False
    return False


print(goes_after("hola", "l", "a"))
print(goes_after("hola", "h", "o"))
print(goes_after("hola", "h", "a"))
