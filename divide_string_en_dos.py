"""
Divide un string dado en pares de caracteres. En caso de no ser
posible completar con '_'. Ej: abcde -> ['ab','cd','e_']
"""


def split_pairs(a):
    """
    input: a (str)
    output: lista (list)
    """
    lista = []
    if len(a) % 2 != 0:
        a = a + "_"
    for i in range(0, len(a), 2):  # Bucle de 0 a len(a)
        lista.append(a[i:i + 2])  # en iteraciones de 2
    return lista


print(split_pairs("abcde"))
