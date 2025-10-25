""" Práctico 8: Manejo de Archivos
Rolando Nebreda 18.350.686 """

#Utiliza utilería de funciones existentes en utils
import utils

#Ejercicio 1
""" 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario  """

# #Imprime los factoriales entre el factorial de 1 y el factorial del número ingresado por el usuario
# #Utiliza 2 funciones recursivas de utils
# utils.imprime_factorial(int(input("Ingrese un número entero: ")))

#Ejercicio 2
""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique.  """

# #Imprime los fibonacci entre el 0 y el fibonacci del número ingresado por el usuario
# #Utiliza 2 funciones recursivas de utils
# utils.imprime_fibonacci(int(input("Ingrese un número entero: ")))


# Ejercicio 3
"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
exponente, utilizando la fórmula n**m = n * n**(m-1). Prueba esta función en un 
algoritmo general. """

# #Solicita ingresar la base y el exponente de la potencia
# base= int(input("Ingrese la base: "))
# exponente= int(input("Ingrese el exponente: "))
# print()

# #Imprime el resultado de la potencia utilizando función recursiva de utils
# print(f"La potencia de {base} elevado a la {exponente} es:", utils.potencia(base, exponente)) 


# Ejercicio 4
""" 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
decimal y devuelva su representación en binario como una cadena de texto.  """

# #Imprime el equivalente en binario de un número decimal utilizando función recursiva de utils
# decimal = int(input("Ingrese un número entero: "))
# print (f"El número {decimal} en binario es:", utils.decimal_a_binario(decimal))


# Ejercicio 5
""" 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es."""

# #Verifica si una palabra dada es un palíndromo utilizando función recursiva de utils
# palabra= input("Ingrese una palabra para verificar si es palíndromo: ")

# if utils.es_palindromo(palabra):
#     print (f"{palabra} es palíndromo")
# else:
#     print (f"{palabra} no es palíndromo")
# print()


# Ejercicio 6
""" 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos.  """

# #Imprime la suma de los dígitos de un entero positivo utilizando función recursiva de utils
# num = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
# print(f"La suma de los dígitos de {num} es {utils.suma_digitos(num)}")
# print()


# Ejercicio 7
""" 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide."""

# #Imprime la cantidad total de bloques de una pirámide según la cantidad de bloques de su base 
# # utilizando función recursiva de utils
# num= int(input("Ingrese la cantidad de bloques de la base: "))
# print(f"La cantidad de bloques de la pirámide es: {utils.contar_bloques(num)}")
# print()

# Ejercicio 8
""" 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número.  """

# #Imprime la cantidad de veces que se repite un dígito dado en un número entero positivo también dado 
# # utilizando función recursiva de utils
# num= int(input("Ingrese un número entero positivo: "))
# digito= int(input("Ingrese el dígito a buscar en el número: "))
# print(f"La cantidad de veces que se repite {digito} en {num} es: {utils.contar_digito(num, digito)}")
# print()


