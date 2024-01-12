"""
Funcion que recibe dos strings y devuelve la 
palabra o palabras comunes en ambos.
"""


def checkio(line1: str, line2: str) -> str:
    """
    input: line1 (str), line2 (str)
    output: palabra o palabras comunes (str)
    """
    line1 = line1.split(",")
    line2 = line2.split(",")
    return ",".join(sorted([i for i in line1 if i in line2]))


print(checkio('hello,world', 'hello,earth'))
print(checkio('one,two,three',
              'four,five,one,two,six,three'))
print(checkio('one,two,three', 'four,five,six'))
