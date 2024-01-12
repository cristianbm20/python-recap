"""
Escribir un programa que pregunte por consola por los productos de una cesta
de la compra, separados por comas, y muestre por pantalla cada uno de los 
productos en una línea distinta.
"""

listaCompra = input(
    "INTRODUCE LA LISTA DE LA COMPRA SEPARANDO CADA ARTICULO CON COMAS: ")
listaSeparada = listaCompra.split(sep=', ')
for producto in listaSeparada:
    print(producto)
