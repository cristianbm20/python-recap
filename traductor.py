"""
Funcion que recibe un string y lo traduce.
"""


def translate(text):
    """
    input: text (str)
    output: text (str)
    """
    vocales = "aeiouy "
    for i in vocales:
        text = text.replace(i * 3, i)
    text = list(text)
    print(text)
    for j, i in enumerate(text):
        print(j)
        print(i)
        if i not in vocales:
            del text[j + 1]
    return ''.join(text)


print(translate("hieeelalaooo"))
