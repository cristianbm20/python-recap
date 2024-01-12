"""
Funcion que devuelve la posicion en la que 
se encuentra un string dentro de otro string.
[row_start,column_start,row_end,column_end]
"""

from itertools import zip_longest


def checkio(text, word):
    """
    input: text (str), word (str)
    output: posicion de la palabra en el texto (list)
    """
    # Primero busca la palabra horizontalmente
    horizontal = text.lower().replace(' ', '').splitlines()
    for i, row in enumerate(horizontal, 1):
        index = row.find(word)
        if index >= 0:
            return [i, index + 1, i, index + len(word)]
    # Si no la encuentra la busca de manera vertical.
    vertical = [''.join(line)
                for line in zip_longest(*horizontal, fillvalue='-')]
    print(vertical)
    for i, col in enumerate(vertical, 1):
        index = col.find(word)
        if index >= 0:
            return [index + 1, i, index + len(word), i]
    return None


print(checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "often"))

print(checkio("""Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.""", "stog"))
