"""
Funcion que mueve el ultimo elemento de una
lista al primer puesto.
"""


def replace_last(line: list) -> list:
    """
    input: line (list)
    output: lista con el ultimo elemento en primer puesto (list)
    """
    return line[-1:] + line[:-1]


print(replace_last([2, 3, 4, 1]))
print(replace_last([1]))
print(replace_last([]))
