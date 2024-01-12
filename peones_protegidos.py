"""
Funcion que devuelva cuantos peones hay a salvo.
"""


def safe_pawns(pawns: set) -> int:
    """
    input: set de posiciones de peones (str)
    output: numero de peones a salvo (int)
    """
    safe_pawns_count = 0
    for i in pawns:
        left = chr(ord(i[0])-1)+str(int(i[1])-1)
        right = chr(ord(i[0])+1)+str(int(i[1])-1)
        safe_pawns_count += left in pawns or right in pawns
    return "Peones a salvo: " + str(safe_pawns_count)


print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
