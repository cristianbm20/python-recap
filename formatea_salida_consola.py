"""
Escribir un programa que pregunte el nombre de un producto, su precio y 
un número de unidades y muestre por pantalla una cadena con el nombre del
producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
el número de unidades con tres dígitos y el coste total con ocho dígitos 
enteros y 2 decimales.
"""

nombreProd = input("INTRODUCE EL NOMBRE DEL PRODUCTO: ")
precioProd = float(input("INTRODUCE EL PRECIO DEL PRODUCTO: "))
unidadesProd = int(input("INTRODUCE UNIDADES DE PRODUCTO: "))
print("{}: {:3d} UNIDADES. PRECIO/UNIDAD: {:9.2f} €. TOTAL: {:11.2f} €")
