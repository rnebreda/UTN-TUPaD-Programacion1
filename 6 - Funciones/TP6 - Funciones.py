""" Práctico 6: Funciones
Rolando Nebreda 18.350.686 """

#Ejercicio 1
""" 1) Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.  """

# def imprimir_hola_mundo():
#     print("Hola Mundo!")
#
# imprimir_hola_mundo()


#Ejercicio 2
""" 2) Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.   """

# def saludar_usuario(nombre):
#     print(f"Hola {nombre}!!")
#
# saludar_usuario(input("Ingrese su nombre: "))


# Ejercicio 3
"""3) Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados. """

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# informacion_personal(nombre= input("Ingrese su nombre: "), apellido= input("Ingrese su apellido: "), \
# edad= input("Ingrese su edad: "), residencia= input("Ingrese su lugar de residencia: "))


# Ejercicio 4
""" 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro
y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como 
parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas 
funciones para mostrar los resultados."""

# def calcular_area_circulo(radio):
#     return round(3.14*radio*radio, 2)
#
# def calcular_perimetro_circulo(radio):
#     return round(2*3.14*radio, 2)
#
# radio=float(input("Ingrese el radio del círculo: "))
#
# print("El perímetro del círculo es", calcular_perimetro_circulo(radio),\
# ", y el área es", calcular_area_circulo(radio))


# Ejercicio 5
""" 5) Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y 
mostrar el resultado usando esta función.  """

# def segundos_a_horas(segundos):
#     return segundos / 3600
#
# horas= segundos_a_horas(int(input("Ingrese la cantidad de segundos: ")))
#
# print(f"La cantidad de horas correspondiente es {round(horas, 2)}")


# Ejercicio 6
""" 6) Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función. """

# def tabla_multiplicar(numero):
#     print()
#     for i in range(1,11):
#         print(f"{i} x {numero} =", i*numero)
#     print()
#
# tabla_multiplicar(int(input("Ingrese el número para el cual desea obtener la tabla: ")))


# Ejercicio 7
"""7) Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara. """

# # Crea la función que devuelve una tupla con los resultados de las operaciones básicas entre 2 números
# def operaciones_basicas(a,b):
#     return (round(a+b, 2), round(a-b, 2), round(a*b, 2), round(a/b, 2))

# # Solicita un número al usuario número (puede ser float y negativo)
# num1= input("Ingrese el primer número: ")

# # Valida si es negativo utilizando la variable auxiliar sin_signo1
# # Si el primer caracter es "-", asigna el valor de num1 sin el signo a sin_signo1
# if len(num1.strip())!=0 and num1.strip()[0]=="-":
#     sin_signo1=num1.strip()[1:]
# else:
#     sin_signo1=num1.strip()

# # Valida que el valor de sin_signo1 sea un numero
# # Repite la solicitud hasta que el dato ingresado sea correcto
# while not sin_signo1.replace(".","",1).isdigit():
#     print("El dato ingresado no es correcto.")
#     num1= input("Ingrese el primer número: ")
#     if len(num1.strip())!=0 and num1.strip()[0]=="-":
#         sin_signo1=num1.strip()[1:]
#     else:
#         sin_signo1=num1.strip()

# # Finalmente convierte el dato en num1 (str) a float
# num1=float(num1)

# # Solicita un número al usuario número (puede ser float y negativo pero distinto de cero)
# num2= input("Ingrese el segundo número (Debe ser distinto de cero): ")

# # Valida si es negativo utilizando la variable auxiliar sin_signo2
# # Si el primer caracter es "-", asigna el valor de num2 sin el signo a sin_signo2
# if len(num2.strip())!=0 and num2.strip()[0]=="-":
#     sin_signo2=num2.strip()[1:]
# else:
#     sin_signo2=num2.strip()

# # Valida que el valor de sin_signo2 sea un numero y distinto de cero
# # Repite la solicitud hasta que el dato ingresado sea correcto
# while not (sin_signo2.replace(".","",1).isdigit()) or float(sin_signo2)==0:
#     print("El dato ingresado no es correcto.")
#     num2= input("Ingrese el segundo número (Debe ser distinto de cero): ")
#     if len(num2.strip())!=0 and num2.strip()[0]=="-":
#         sin_signo2=num2.strip()[1:]
#     else:
#         sin_signo2=num2.strip()

# # Finalmente convierte el dato en num2 (str) a float
# num2=float(num2)

# # Utiliza la función operaciones_basicas para generar una tupla con los resultados
# resultados= operaciones_basicas(num1, num2)

# # Muestra los resultados accediendo a la tupla por sus índices
# print()
# print(f"Los resultados de las operaciones básicas entre {num1} y {num2} son:")
# print(f"Suma = {resultados[0]}, Resta = {resultados[1]}, \
# Multiplicación = {resultados[2]}, División = {resultados[3]}")


# Ejercicio 8
""" 8) Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar 
a la función para mostrar el resultado con dos decimales.  """

# #Crea la función. Los argumentos son datos tipo string, pero retorna un float (redondeado a 2 decimales)
# def calcular_imc(peso, altura):
#     return round(peso / (altura * altura), 2)

# # Solicita el peso al usuario y valida que el dato ingresado sea un número no negativo (float)
# peso = input("Ingrese su peso (en kilogramos): ")

# # Repite la solicitud hasta que el dato ingresado sea correcto
# while not peso.replace(".","",1).isdigit():
#     print("El dato ingresado no es correcto.")
#     peso = input("Ingrese su peso (en kilogramos): ")

# # Solicita la altura al usuario y valida que el dato ingresado 
# # sea un número no negativo y distinto de cero (float)
# altura = input("Ingrese su altura (en metros): ")

# # Repite la solicitud hasta que el dato ingresado sea correcto
# while not (altura.replace(".","",1).isdigit()) or float(altura)==0:
#     print("El dato ingresado no es correcto.")
#     altura = input("Ingrese su altura (en metros): ")

# # Muestra el IMC de la persona utilizando los datos ingresados de peso y altura (str) convertidos a float
# print()
# print("El valor de su IMC es:", calcular_imc(float(peso), float(altura)))


# Ejercicio 9
""" 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.  """

# # Crea la función que transforma un valor en °C a °F
# def celsius_a_fahrenheit(celsius):
#     return round (celsius * 9 / 5 + 32, 2)

# # Solicita una temperatura en °C al usuario (puede ser float y negativo)
# celsius= input("Ingrese una temperatura en °C: ")

# # Valida si es negativo utilizando la variable auxiliar sin_signo
# # Si el primer caracter es "-", asigna el valor de celsius sin el signo a sin_signo
# if len(celsius.strip())!=0 and celsius.strip()[0]=="-":
#     sin_signo=celsius.strip()[1:]
# else:
#     sin_signo=celsius.strip()

# # Valida que el valor de sin_signo sea un numero
# # Repite la solicitud hasta que el dato ingresado sea correcto
# while not sin_signo.replace(".","",1).isdigit():
#     print("El dato ingresado no es correcto.")
#     celsius= input("Ingrese una temperatura en °C: ")
#     if len(celsius.strip())!=0 and celsius.strip()[0]=="-":
#         sin_signo=celsius.strip()[1:]
#     else:
#         sin_signo=celsius.strip()

# # Finalmente convierte el dato en celsius ya validado (pero aun como str) a float
# celsius=float(celsius)

# # Muestra el equivalente del valor celsius en °F 
# print(f"{celsius} °C equivale a", celsius_a_fahrenheit(celsius)," °F")


# Ejercicio 10
""" 10) Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta función.  """

# # Crea la función que calcula el promedio de 3 números enteros retorna un float redondeado a 2 decimales
# def calcular_promedio(a, b, c):
#     return round((a + b + c) / 3, 2)

# # Utiliza la lista numeros como auxiliar para almacenar los 3 números
# numeros=[]

# # Utiliza un for para repetir la solicitud al usuario y la validación
# for i in range(1, 4):

#     # La variable orden (str) permite cambiar el ordinal en la solicitud al usuario
#     match i:
#         case 1: orden= "primer"
#         case 2: orden= "segundo"
#         case 3: orden= "tercer"

#     # Solicita un número al usuario y valida que el dato ingresado sea un número no negativo (int)
#     num = input(f"Ingrese el {orden} número (entero positivo): ")

#     # Repite la solicitud hasta que el dato ingresado sea correcto
#     while not num.isdigit():
#         print("El dato ingresado no es correcto.")
#         num = input(f"Ingrese el {orden} número (entero positivo): ")

#     # Agrega el número ya validado a la lista como número entero
#     # Al salir del for la lista numeros contendrá 3 números enteros positivos
#     numeros.append(int(num))

# # Muestra los valores ingresados accediendo a los elementos de la lista por sus índices
# # Utiliza la fórmula calcular_promedio con los parámetros obtenidos de los valores de la lista
# print(f"El promedio de {numeros[0]}, {numeros[1]} y {numeros[2]} es",\
# calcular_promedio(numeros[0], numeros[1], numeros[2]))

