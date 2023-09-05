# #Operadores aritméticos
# print(2 + 2)#Suma
# print(4 - 1)#Resta
# print(3 * 7)#Multiplicación
# print(15 / 2)#División
# print(11 % 4)#Once módulo cuatro - Residuo de div
# print(11 // 4)#División de piso (Cuánto cabe un número en otro)
# print(2 ** 3)#Potencia

# #Operadores en cadenas de texto
# print("Hola" + " mundo.")#Concatenación
# print("Hola" * 3)#Repetición
# print("Hola" + " mundo" * 3)

# #Operadores de comparación
# print("Hola" == "hola")#Igual qué
# print("Hola" != "hola")#Diferente qué
# print(3 > 11)#Mayor qué
# print(11 >= 10)#Mayor o igual qué

# #Operadores de existencia
# print("ola" in "hola")#Existencia
# print("ola" not in "hola")#Inexistencia

# #Operadores booleanos
# print(True or False)#or - Verifica que cumpla una de las condiciones
# print(True and False)#and - Verifica que se cumplan ambas

#Operador de asignación
# x = 1
# x += 2#Operador de asignación suma
# x *= 3#Operador de asignación multiplicación
# x %= 4#Operador de asignación módulo
# print(x)

#Orden de aplicación de los operadores
#1 - Paréntesis ()
#2 - Potencia**
#3 - Mult-Div-Div piso-Módulo
#4 - Sumas y restas
#5 - Dos operadores del mismo nivel se resuelven de izq a der

x = 6 * 5 + 8 / 2 ** 4
print(x)