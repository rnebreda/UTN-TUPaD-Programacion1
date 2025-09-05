""" Práctico 4: Estructuras Repetitivas
Rolando Nebreda 18.350.686 """

#Ejercicio 1
""" 1) Crea un programa que imprima en pantalla todos los números 
enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden 
creciente, mostrando un número por línea. """

##El valor de LIMITE será el argumento en la función range
##valor hasta el cual se va a imprimir (para este ejercicio 100)
# LIMITE = 100
#
# for i in range (LIMITE + 1):
#     print (i)

#Ejercicio 2
""" 2) Desarrolla un programa que solicite al usuario un número entero 
y determine la cantidad de dígitos que contiene.  """

# num = int(input("Ingrese un número entero: "))

# # utilizo el valor absoluto del número ingresado, 
# # en caso de que el usuario ingrese un entero negativo
# # deja el numero ingresado sin modificar para utilizarlo
# # en el print al final
# absoluto = abs(num)
# #si el usuario ingresa un número de 1 sola cifra
# #el valor de cuenta_cifras será 1
# cuenta_cifras = 1
#
# while absoluto >= 10:
#     #cada vez que divida por 10 cuenta_cifras se incrementará en 1
#     absoluto /= 10
#     cuenta_cifras += 1
# # cuando el valor de absoluto sea menor a 10 sale del bucle
# # e imprime la cantidad de cifras del número ingresado
# print(f"la cantidad de cifras del número {num} es {cuenta_cifras}")


# Ejercicio 3
"""3) Escribe un programa que sume todos los números enteros
comprendidos entre dos valores dados por el usuario, 
excluyendo esos dos valores."""

# num1 = int(input("Ingrese un número entero: "))
# num2 = int(input("Ingrese el segundo número entero: "))
# bandera = True
# suma = 0
# # considera la posibilidad de que el usuario ingrese 
# # los números en cualquier orden.
# hay_enteros_entre = abs(num1-num2)>1
# # al menor (min) como argumento de la función range le sumo 1 
# # para que lo excluya
# # al mayor (max) lo tomo tal cual porque el bucle for se repetira 
# # hasta el valor del mayor - 1
# if hay_enteros_entre and num1 > num2:
#     max = num1
#     min = num2+1
# elif hay_enteros_entre and num2 > num1:
#     max = num2
#     min = num1+1
# else:
#     #si no hay enteros entre los números ingresados emite un mensaje
#     # y asigna el valor False a bandera para que el bucle for no se ejecute
#     print(f"No hay enteros entre {num1} y {num2}")
#     bandera = False
#
# if bandera:
#     #se ejecuta solo si hay enteros entre los 2 números ingresados
#     for i in range (min, max):
#         suma += i
#     print(f"la suma de los enteros comprendidos\
#  entre {num1} y {num2} es:", suma)

# Ejercicio 4
""" 4) Elabora un programa que permita al usuario ingresar números enteros 
y los sume en secuencia. El programa debe detenerse y mostrar el total 
acumulado cuando el usuario ingrese un 0."""

# num1 = int(input("Ingrese un número entero (ingrese 0 para finalizar): "))
# suma=0
#
# while num1 !=0:
#     suma += num1
#     num1 = int(input("Ingrese un número entero (ingrese 0 para finalizar): "))
# print("El resultado de la suma de los números ingresados es:",suma)

# Ejercicio 5
""" 5) Crea un juego en el que el usuario deba adivinar un número 
aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos 
intentos fueron necesarios para acertar el número. """

# #importa la libreria random para utilizar la funcion randint()
# import random
# #esta funcion entrega un entero al azar entre el min y el max 
# # (en este caso entre 0 y 9 )
# incognita = random.randint(0, 9)
# #
# # inicializo "intento" con 1 ya que el bucle se ejecutará al menos una vez
# intento = 1
# #para iniciar el juego asigno a la variable "ingresado" 
# # un valor fuera del rango
# ingresado = 99999999999999
# #
# #Inicio del juego
# print("Averigua el número escondido")
# #El juego terminará cuando "ingresado" sea igual a "incognita"
# while ingresado != incognita:
#     ingresado = int(input("Ingresa un número entero entre 0 y 9: "))
#     # con la variable booleana "valido" se asegura que 
#     # el valor ingresado esté dentro del rango. Si nó se perderá un turno.
#     valido = 0 <= ingresado <= 9
#     if not valido:
#         #si se ingresa un número fuera del rango, se pierde un intento y continúa
#         print("El número ingresado debe ser entero entre 0 y 9. Perdiste un intento")
#         intento += 1
#     elif ingresado == incognita:
#         #si se averiguó el número escondido, finaliza.
#         print(f"Felicitaciones!!. Encontraste el número escondido {incognita} en {intento} intentos")
#     else:
#         #si no se averiguo el número, incrementa intento y continúa probando
#         print("Fallaste!!. Probá nuevamente")
#         intento += 1

# Ejercicio 6
""" 6) Desarrolla un programa que imprima en pantalla todos los números 
pares comprendidos entre 0 y 100, en orden decreciente."""

# #El valor de LIMITE será el primer argumento en la función range
# #valor desde el cual comenzará a imprimir (para este ejercicio 100)
# LIMITE = 100
# # el segundo argumento en la funcion range es -1 
# # para que el cero también se imprima
# # el tercer argumento es -2 para que decremente de a 2 unidades
# for i in range (LIMITE,-1,-2):
#     print (i)

# Ejercicio 7
"""7) Crea un programa que calcule la suma de todos los números 
comprendidos entre 0 y un número entero positivo indicado por el usuario."""

# num1 = int(input("Ingrese un número entero positivo: "))
# suma = 0
# validado = num1 > 0
# if validado:
#         #Para este ejercicio, el número ingresado por el usuario se incluye en la suma
#     for i in range (num1 + 1):
#         suma += i
#     print(f"la suma de los enteros comprendidos\
#  entre {num1} y 0 es:", suma)
# else:
#     #si el número ingresado es menor o igual a cero muestra un mensaje
#     print("El número ingresado debe ser mayor que cero")


# Ejercicio 8
""" 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio). """

# LIMITE = 100
# ingresado = 0
# cuenta_positivos = 0
# cuenta_negativos = 0
# #Para este ejercicio el 0 se considera PAR y POSITIVO
# cuenta_pares = 0
# cuenta_impares = 0
#
# for i in range(LIMITE):
#     ingresado = int(input("Ingrese un número entero: "))
#     if ingresado>= 0:
#         cuenta_positivos += 1
#     else:
#         cuenta_negativos +=1
#
#     if ingresado % 2 == 0:
#         cuenta_pares += 1
#     else:
#         cuenta_impares += 1
#
# print()
# print(f"De los {LIMITE} números ingresados:")
# print(f"{cuenta_pares} son pares")
# print(f"{cuenta_impares} son impares")
# print(f"{cuenta_positivos} son positivos")
# print(f"{cuenta_negativos} son negativos")

# Ejercicio 9
""" 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor). """

# LIMITE = 100
# ingresado = 0
# suma = 0

# for i in range(LIMITE):
#     ingresado = int(input("Ingrese un número entero: "))
#     suma += ingresado

# print(f"El promedio de los {LIMITE} números ingresados es {suma/LIMITE}")

# Ejercicio 10
""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

# #importa la biblioteca math para utilizar la función floor()
# import math
# num1 = int(input("Ingrese un número entero positivo: "))

# #utiliza una variable auxiliar, a fin de conservar el valor de num1
# auxiliar = num1

# # utiliza num2 para almacenar las cifras que se van obteniendo de auxiliar
# # el resto de auxiliar dividido 10 entrega la última cifra de auxiliar y la agrega a num2
# num2= auxiliar % 10

# # En el bucle while divido en cada loop a auxiliar por 10 y el resto (ultima cifra)
# #  la va agregando a num2 multiplicando por 10 el contenido de num2 hasta ese momento antes de sumar.
# # Sale del bucle cuando auxiliar es menor que 10
# while auxiliar >= 10:
#     auxiliar = math.floor(auxiliar / 10)
#     num2= num2*10 + auxiliar % 10
# # Finalmente se imprime num1 y su invertido que es num2
# print(f"El número {num1} invertido es {num2}")
