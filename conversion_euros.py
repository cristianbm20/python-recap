"""
Escribir un programa que pregunte por consola el precio de un producto en 
euros con dos decimales y muestre por pantalla el número de euros y el 
número de centimos del precio introducido.
"""

import math

precio = float(input("INTRODUCE EL PRECIO DE UN PRODUCTO CON DOS DECIMALES: "))
centimos, euros = math.modf(precio)
euros = int(euros)
centimos = int(round(centimos, 2)*100)


print(f"EL PRECIO ES {euros} EUROS Y {centimos} CENTIMOS.")
