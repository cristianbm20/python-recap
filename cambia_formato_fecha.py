"""
Escribir un programa que pregunte la usuario la fecha de su nacimiento 
en formato dd/mm/aaaa y muestre por pantalla el día, el mes y el año.
Adaptar el programa anterior para que también funcione cuando el día 
o el mes se introduzcan con un solo carácter.

Primera versión.

fecha_nac = input("INTRODUZCA FECHA DE NACIMIENTO EN FORMATO DD/MM/AAAA: ")
dia = fecha_nac[0:2]
meses = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO",
    "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
mes = int(fecha_nac[3:5])
mes_en_letra = meses[mes - 1]
year = fecha_nac[-4:]
print("FECHA DE NACIMIENTO: {} DE {} DEL AÑO {}".format(dia, mes_en_letra, year))
"""

# Segunda versión.

fecha_nac = input("INTRODUZCA FECHA DE NACIMIENTO EN FORMATO DD/MM/AAAA: ")
fecha_separada = fecha_nac.split(sep='/', maxsplit=3)
dia = int(fecha_separada[0])
mes = int(fecha_separada[1])
year = int(fecha_separada[2])
if (dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12) and (year > 0):
    meses = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO",
             "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
    mes_en_letra = meses[mes - 1]
    print(f"FECHA DE NACIMIENTO: {dia} DE {mes_en_letra} DEL AÑO {year}")
else:
    print("LA FECHA INTRODUCIDA ES ERRONEA")
