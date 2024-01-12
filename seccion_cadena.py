"""
Los teléfonos de una empresa tienen el siguiente formato prefijo-numero-extension
donde el prefijo es el codigo del pais +34, y la extension tiene dos dígitos
(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de
teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo
y la extensión.
"""

num = input("INTRODUZCA NUMERO DE TELÉFONO CON EL FORMATO +XX-XXXXXXXXX-XX: ")
print(num[4:-3])
