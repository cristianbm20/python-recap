"""
Funcion que corrige frases pasadas como argumento.
La primera letra de la frase la convierte en mayuscula
si fuera necesario y añade un punto al final.
"""


def correct_sentence(text: str) -> str:
    """
    input: text (str)
    output: text (str)
    """
    lista = text.split()
    lista[0] = lista[0].capitalize()
    text = " ".join(lista)
    if text[len(text)-1] != ".":
        text = text + "."
    return text


print(correct_sentence("Saludos viajeros."))
print(correct_sentence("saludos viajeros."))
print(correct_sentence("Saludos viajeros"))
print(correct_sentence("welcome to New York"))
