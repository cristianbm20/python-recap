"""
funcion que devuelve True si el número dado como
argumento es par y devuelve False si es impar.
"""


def is_even(num: int) -> bool:
    """
    input: num (int)
    output: True si num es par, False si num es impar (bool)
    """
    if num % 2 != 0:
        return False
    return True


print(is_even(3))
print(is_even(8))
