"""
Escribir un programa que pida al usuario una frase por consola y una vocal,
y después muestre por pantalla la misma frase pero con la vocal introducida
en mayuscula.
"""

frase = input("INTRODUZCA UNA FRASE: ")
vocal = input("INTRODUZCA UNA VOCAL: ")
print(frase.replace(vocal, vocal.upper()))
