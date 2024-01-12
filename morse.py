"""
Funcion que recibe un string de simbolos morse y lo 
tranduce mediante un diccionario.
"""

MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "": " "
}


def morse_decoder(code):
    """
    input: code (str)
    output: texto traducido (str)
    """
    values = list(MORSE.values())
    keys = list(MORSE.keys())
    code_list = code.split(sep=" ")
    text = []

    for i in code_list:
        if i in keys:
            value = keys.index(i)
            text.append(values[value])
    text = "".join(text)
    text = text.replace("  ", " ")
    return text.capitalize()


print(morse_decoder("... --- ..."))
print(morse_decoder("... --- -- .   - . -..- -"))
print(morse_decoder("... --- -- .  - . -..- -"))
print(morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"))
