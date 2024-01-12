"""
Funcion que obtiene los numeros de un string y los suma.
"""


def sum_numbers(text: str) -> int:
    """
    input: text (str)
    output: suma de numeros (int)
    """
    num = []
    lista = text.split()
    for i in lista:
        if i.isdigit():
            num.append(float(i))
    return int(sum(num))


print(sum_numbers("saludos esto es 23 mas 10"))
