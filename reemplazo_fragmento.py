"""
Escribir un programa que pregunte el correo electrónico del usuario por consola 
y muestre por pantalla otro correo electrónico con el mismo nombre(la parte delante de
@) pero con dominio ceu.es
"""

mail = input("INTRODUZCA SU DIRECCION DE CORREO ELECTRÓNICO: ")
DOMINIO = "@ceu.es"
print(mail[:mail.find("@")] + DOMINIO)
