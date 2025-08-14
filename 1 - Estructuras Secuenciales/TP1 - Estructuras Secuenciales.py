""" Práctico 1: Estructuras secuenciales
Rolando Nebreda 18.350.686 """

#Ejercicio 1
""" 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. """  

#print ("Hola Mundo!")

#Ejercicio 2
""" 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
realizar la impresión por pantalla.  """

#nombre = input("Ingrese su nombre")
#print (f"Hola {nombre}!")

#Ejercicio 3
""" 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
la impresión por pantalla. """

#nombre = input("Ingrese su nombre: ")
#apellido = input("Ingrese su apellido: ")
#edad = input("Ingrese su edad: ")
#residencia = input("Ingrese su lugar de residencia: ")
#print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
""" 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
su perímetro. """ 

#radio = float (input("Ingrese el radio del círculo: "))
#area = 3.14 * (radio**2)
#perimetro = 3.14 * 2 * radio
#print(f"El área del círculo es {area} y el perímetro {perimetro}")

#Ejercicio 5
""" 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
cuántas horas equivale.  """

#segundos = int (input("Ingrese la cantidad de segundos: "))
#horas = segundos / 3600
#print (f"{segundos} segundos equivalen a {horas} horas")

#Ejercicio 6
""" 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
multiplicar de dicho número.  """

# numero = int (input("Ingrese un número entero (1-10): "))
# print (f"Tabla del número {numero}")
# print (f" 1 * {numero} = ", numero*1)
# print (f" 2 * {numero} = ", numero*2)
# print (f" 3 * {numero} = ", numero*3)
# print (f" 4 * {numero} = ", numero*4)
# print (f" 5 * {numero} = ", numero*5)
# print (f" 6 * {numero} = ", numero*6)
# print (f" 7 * {numero} = ", numero*7)
# print (f" 8 * {numero} = ", numero*8)
# print (f" 9 * {numero} = ", numero*9)
# print (f"10 * {numero} = ", numero*10)

#Ejercicio 7
""" 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. """

# num1 = int(input("Ingrese el primer número entero (distinto de cero): "))
# num2 = int(input("Ingrese el segundo número entero (distinto de cero): "))
# print (f" La suma de {num1} + {num2} es = ", num1+num2)
# print (f" La resta de {num1} - {num2} es = ", num1-num2)
# print (f" La multiplicación de {num1} * {num2} es = ", num1*num2)
# print (f" La división de {num1} / {num2} es = ", num1/num2)

#Ejercicio 8
""" 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
modo:   IMC = peso en kg / (altura en m)**2"""

# altura= float (input("Ingrese su altura (en metros): "))
# peso= float (input("Ingrese su peso (en kg): "))
# masa_corporal= peso/(altura**2)
# print(f"Su IMC es: {masa_corporal} kg/m2")

#Ejercicio 9
""" 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:  
F = 9/5 C + 32"""

# celsius = float (input("Ingrese la Temperatura en °C: "))
# fahrenheit = (9*celsius/5)+32
# print(f"{celsius} °C equivalen a {fahrenheit} °F")

# Ejercicio 10
""" 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
dichos números.  """

# num1= float(input("Ingrese el primer número: "))
# num2= float(input("Ingrese el segundo número: "))
# num3= float(input("Ingrese el último número: "))
# promedio = (num1+num2+num3)/3
# print(f"El promedio de {num1}, {num2} y {num3} es: {promedio}")

""" FIN """