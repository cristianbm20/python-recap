"""
Determina el digito mayor de un numero dado.
"""


def max_digit(num: int):
    """
    input: num (int)
    output: max (int)
    """
    num_list = [int(a) for a in str(num)]
    max_num = 0
    for i in num_list:
        if i > max_num:
            max_num = i
    return max_num


print(max_digit(845))
