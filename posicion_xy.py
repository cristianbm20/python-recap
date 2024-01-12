"""
Funcion que recibe unas instrucciones de movimiento
mediante un string. Las letras f(hacia delante), 
b(hacia atras), l(izq) y r(derecha). La funcion
devuelve la posicion final (x, y)
"""

from typing import Tuple


def follow1(instructions: str) -> Tuple[int, int]:
    """
    input: instructions (str)
    output: posicion final (tuple)
    """
    x = instructions.count("r")-instructions.count("l")
    y = instructions.count("f")-instructions.count("b")
    return (x, y)


print(follow1("ffbf"))
print(follow1("fflff"))
