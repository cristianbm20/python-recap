"""
Funcion que devuelva la parte de una cadena comprendida
entre los dos caracteres que se le pasan como argumento.

"""


def between_markers(text: str, begin: str, end: str) -> str:
    """
    input: cadena de texto, marca inicial, marca final
    output: cadena de texto entre las marcas
    """
    if not begin in text and not end in text:
        return text
    elif begin in text and not end in text:
        begin_index = text.index(begin) + len(begin)
        return text[begin_index:]
    elif not begin in text and end in text:
        end_index = text.index(end)
        return text[:end_index]
    else:
        begin_index = text.index(begin) + len(begin)
        end_index = text.index(end)
        return text[begin_index:end_index]


print(between_markers('No[/b] hi', '[b]', '[/b]'))
