"""Utilería de funciones para recursividad"""

#Función recursiva que calcula el factorial de un número dado
def factorial(num): 
    if num == 0: 
        return 1 
    else: 
        return num * factorial(num - 1)

#Funcion recursiva que imprime los factoriales 
# desde el factorial de un número dado hasta el factorial de 1
def imprime_factorial(num):
    if num > 0:
        print(f"Factorial de {num} =", factorial(num))
        imprime_factorial(num-1)

#Función recursiva que calcula el fibonacci de un número dado
def fibonacci(num): 
    if num == 0 or num == 1: 
        return num 
    else: 
        return fibonacci(num - 1) + fibonacci(num - 2)

#Funcion recursiva que imprime los fibonacci 
# desde el fibonacci de un número dado hasta el fibonacci de 0
def imprime_fibonacci(num):
    if num >= 0:
        print(f"Fibonacci de {num} =", fibonacci(num))
        imprime_fibonacci(num-1)

#Función recursiva que calcula la potencia de un número dado elevado a un exponente dado
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)
    
#Función recursiva que convierte un número decimal dado a binario
def decimal_a_binario(decimal):
    if decimal < 2:
        return str(decimal)
    else:
        return  decimal_a_binario(decimal//2) + str(decimal % 2)

#Función recursiva que verifica si una palabra dada es palíndromo
#Devuelve True si es palíndromo y False si no lo es.
def es_palindromo(palabra):

    #pasa la palabra a minúsculas
    palabra.lower()

    #Si es de un solo caracter o vacía, es palíndromo y devuelve True
    if len(palabra) <= 1:
        return True
    #Si tiene más de un caracter, compara el primer caracter con el último
    #Si son distintos, no es palíndromo y devuelve False
    elif palabra[0] != palabra[-1]:
        return False
    #Si los caracteres son iguales, devuelve el resultado de
    #evaluar la palabra sin el primer y último caracter recursivamente
    #hasta que o sea Falso, o hasta que el largo de la palabra sea <= a 1.
    else:
        return es_palindromo(palabra[1:-1])

#Función recursiva que devuelve la suma de los dígitos de un entero positivo dado
def suma_digitos(num):

    #Si es menor que 10 (un solo dígito) devuelve el valor de ese dígito
    if num < 10:
        return num
    else:
        #Si es mayor a 10 suma el último dígito y vuelve a calcular la función 
        # con el valor de la división entera del número en forma recursiva
        return num%10 + suma_digitos(num//10)
    
#Función recursiva que devuelve el total de bloques de una pirámide 
# de acuerdo a la cantidad de bloques de su base (valores enteros positivos)
def contar_bloques(num):
    
    if num == 1 or num == 0:
        return num
    else:
        return num + contar_bloques(num-1)
    

#Función recursiva que devuelve la cantidad de veces que un dígito dado 
# se repite en un número entero positivo también dado
def contar_digito(num, digito):

    #Caso base: Si es menor que 10 (una sola cifra) 
    # compara el valor de esa cifra con el dígito dado
    #Si es igual el valor de la función es 1. Si no es 0.
    if num < 10:
        return 1 if num == digito else 0

    else:
        #Si es mayor o igual que 10 (tiene más de una cifra)
        #obtiene la última cifra y la compara con el dígito dado
        if num%10 == digito:
            #Si es igual suma 1 y ejecuta recursivamente la función con la división entera
            # por 10 como argumento (num//10)
            return 1 + contar_digito(num//10, digito)
        else:
            #Si no es igual al dígito ejecuta la función sin sumar
            return contar_digito(num//10, digito)

    