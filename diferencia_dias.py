"""
Funcion que calcula la diferencia en días entre dos
fechas dadas. 
"""

from datetime import date


def days_diff(a, b):
    """
    input: a (tuple), b (tuple)
    output: diferencia en días (int)
    """
    first = list(a)
    second = list(b)
    first_date = date(first[0], first[1], first[2])
    second_date = date(second[0], second[1], second[2])
    return abs((second_date - first_date).days)


print(days_diff((2021, 12, 21), (1995, 4, 20)))
