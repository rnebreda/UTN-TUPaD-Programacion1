""" Práctico 5: Listas
Rolando Nebreda 18.350.686 """

#Ejercicio 1
""" 1) Crear una lista con las notas de 10 estudiantes. 
• Mostrar la lista completa. 
• Calcular y mostrar el promedio. 
• Indicar la nota más alta y la más baja.  """

# # Se crea la lista "notas" vacía.
# notas = []
# suma=0
# mayor=0
# menor=9999
#
# for i in range (10):
#     #Para este ejercicio se asume (sin validar) que las notas ingresadas
#     # son enteros positivos entre 0 y 10
#     notas.append(int(input("Ingrese la nota de un alumno: ")))
#     suma = suma + notas[i]
#     if notas[i] < menor:
#         menor = notas[i]
#     if notas[i] > mayor:
#         mayor = notas[i]

# print()   
# print("El promedio de las notas ingresadas es:",suma/10)
# print(f"La nota más alta ingresada es {mayor} y la más baja es {menor}")

#Ejercicio 2
""" 2) Pedir al usuario que cargue 5 productos en una lista. 
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.   """

# productos = []
#
# for i in range (5):
#     productos.append(input("Ingrese un producto: "))
#
# print()
# productos.sort()
# print(productos)
# print()
# productos.remove(input("Cuál producto desea eliminar? "))
# print()
# print(productos)
# print()


# Ejercicio 3
"""3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
• Crear una lista con los pares y otra con los impares. 
• Mostrar cuántos números tiene cada lista. """

# #importa la librería random para usar el método randint
# import random
# # Crea listas vacías para los aleatorios, pares e impares
# aleatorios=[]
# pares=[]
# impares=[]
#
# for i in range (15):
#     #para cada i del for carga un entero aleatorio entre 1 y 100 a la lista
#     aleatorios.append(random.randint(1, 100))
#     if aleatorios[i]%2 == 0:
#         # si es par tambien lo carga en pares
#         pares.append(aleatorios[i])
#     else:
#         # si es impar lo carga tambien en impares
#         impares.append(aleatorios[i])
#
# print("Lista original: ")
# print(aleatorios)
# print()
# # utiliza len() para ver la cantidad de elementos de cada lista
# print(f"La lista contiene {len(pares)} pares y {len(impares)} impares.")
# print()
# print("Lista de pares: ")
# print(pares)
# print()
# print("Lista de impares: ")
# print(impares)
# print()


# Ejercicio 4
""" 4) ) Dada una lista con valores repetidos:
    datos=[1, 3, 5, 3, 7, 1, 9, 5, 3]
• Crear una nueva lista sin elementos repetidos. 
• Mostrar el resultado. ."""

# datos=[1, 3, 5, 3, 7, 1, 9, 5, 3]
# sin_repetidos=[]
#
# #recorre la lista datos con un bucle for
# for i in datos:
#     #para cada elemento busca si ya está en la lista sin_repetidos
#     #si es así salta al siguiente bucle del for sin hacer nada
#     if i in sin_repetidos:
#         continue
#     else:
#         #si no está en sin_repetidos lo agrega
#         sin_repetidos.append(i)
#
# print()
# print("La lista sin repetidos es: ")
# print(sin_repetidos)
# print()


# Ejercicio 5
""" 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
• Mostrar la lista final actualizada.  """

# alumnos=[]
# modfica=""
# alumno=""
#
# for i in range(8):
#     alumnos.append(input("Ingrese el nombre de un alumno del curso: "))
#
# print()
# print("La lista de alumnos es: ")
# print(alumnos)
# print()
# # modifica indicará si desea agragar o quitar con "S" / "N" no modifica
# # otro valor avisa que es erroneo y sale del programa sin modificar
# modifica=(input("Desea agregar o quitar un alumno de la lista? (S=Si/N=No): ")).upper()
#
# if modifica == "S":
#     alumno=(input("Ingrese el nombre del alumno a agregar o quitar: "))
#
#     # asume que si el nombre ingresado está en la lista lo tiene que quitar
#     if alumno in alumnos:
#         alumnos.remove(alumno)
#       
#     else:
#         #si por el contrario el alumno no está en la lista lo agrega
#         alumnos.append(alumno)
#
#     print("La lista se ha modificado")
#     print()
#
# elif modifica == "N":
#     print ("La lista no se ha modificado")
# else:
#     print ("El valor ingresado no es correcto. La lista no se ha modificado")
#
# print(alumnos)
# print()


# Ejercicio 6
""" 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha 
(el último pasa a ser el primero). """

# numeros=[10, 20, 30, 40, 50, 60, 70]
#
# #Para este ejercicio usa la asignación multiple para realizar intercambios
# #entre elementos de la lista sin necesidad de utilizar una variable auxiliar
# #empieza intercambiando el elemento de la posision 1 con el de la posición 0
# #este ya que da en el lugar deseado. Siempre el elemento que está en la
# #posición 0, va a quedar en su posición original + 1.
# #Al finalizar el for, el último elemento queda en la posición 0
# #De esta manera recorre la lista una sola vez
# for i in range(1, len(numeros)):
#     numeros[0], numeros[i]=numeros[i], numeros[0]
#
# print(numeros)


# Ejercicio 7
"""7) Crear una matriz (lista anidada) de 7x2 con las temperaturas 
mínimas y máximas de una semana. 
• Calcular el promedio de las mínimas y el de las máximas. 
• Mostrar en qué día se registró la mayor amplitud térmica. """

# #dias_semanas y temperaturas son auxiliares para solicitar los datos al usuario
# dias_semana=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
# temperaturas=["mínima", "máxima"]
# #matriz_temperaturas es donde se van a almacenar las temperaturas diarias 
# # de todos los días de la semana
# matriz_temperaturas=[]
# #matriz_diaria es una lista auxiliar que me va a cargar los datos 
# # de un solo día en el bucle for
# matriz_diaria=[0, 0]
# #variables y acumuladores para los resultados
# amplitud_maxima=0
# dia_mayor_amplitud=""
# suma_minimas=0
# suma_maximas=0
#
# #El bucle for recorre los días de la semana
# for dia in (dias_semana):
#     #por cada día se cargan en la matriz_diaria auxiliar 
#     # los valores de temperatura mínima y máxima de ese día
#     for i in range(2):
#         matriz_diaria[i]= int(input(f"Ingrese la temperatura {temperaturas[i]} del día {dia}: "))
#  
#     #luego compara la amplitud de ese día con la almacenada en amplitud_maxima 
#     # y guarda la mayor y el nombre del día
#     if amplitud_maxima < (matriz_diaria[1]-matriz_diaria[0]):
#         amplitud_maxima = matriz_diaria[1]-matriz_diaria[0]
#         dia_mayor_amplitud = dia
#
#     #finalmente realiza las sumas de mínimas, la de máximas,  
#     # agrega los valores de cada día a la matríz de temperaturas y
#     #limpia la matriz auxiliar
#     suma_minimas += matriz_diaria[0]
#     suma_maximas += matriz_diaria[1]
#     matriz_temperaturas.append(matriz_diaria)
#     matriz_diaria=[0, 0]
#
# print()
# print(f"El día de mayor amplitud térmica fue el {dia_mayor_amplitud}")
# print(f"La amplitud máxima fue de {amplitud_maxima} grados")
# #redondea los promedios a 2 decimales
# print("El promedio de las temperaturas mínimas fue:", round((suma_minimas/7),2))
# print("El promedio de las temperaturas máximas fue:", round((suma_maximas/7),2))
# print()
# print(matriz_temperaturas)


# Ejercicio 8
""" 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
• Mostrar el promedio de cada estudiante. 
• Mostrar el promedio de cada materia.  """

# #matriz de estudiantes y de materias
# estudiantes= ["Carlos", "María", "Juan", "Lidia", "Fernando"]
# materias= ["Ciencias", "Inglés", "Historia"]
# #auxiliar va a cargar las notas de cada estudiantes en una fila de la matriz
# auxiliar= [0, 0, 0]
# #matriz con todas las notas de todos los alumnos
# matriz_notas= []
# # variable auxiliar para almacenar las sumas antes de calcular los promedios
# suma_notas=0
#
# #carga la matriz con la notas en cada fila de un estudiante
# for estudiante in estudiantes:
#     for i in range(len(materias)):
#         auxiliar[i]= int(input(f"Ingrese la nota de {materias[i]} del alumno {estudiante}: "))
#     #agrega la lista auxiliar a la matriz de notas
#     matriz_notas. append(auxiliar)
#     #limpia auxiliar
#     auxiliar=[0, 0, 0]
# #imprime la matriz completa
# print(matriz_notas)
# print()
#
# print("Promedio por estudiante")
# #recorre cada fila y suma las notas de cada estudiante
# for i in range(len(estudiantes)):
#     for j in range(len(materias)):
#         suma_notas += matriz_notas[i][j]
#
#     print(f"{estudiantes[i]}:", suma_notas/len(materias))
#     suma_notas= 0
# print()
#
# print("Promedio por materia")
# #recorre cada columna y suma las notas por materia
# for j in range(len(materias)):
#     for i in range(len(estudiantes)):
#         suma_notas += matriz_notas[i][j]
#
#     print(f"{materias[j]}:", suma_notas/len(estudiantes))
#     suma_notas= 0
# print()


# Ejercicio 9
""" 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
• Inicializarlo con guiones "-" representando casillas vacías. 
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
• Mostrar el tablero después de cada jugada.  """

# #matrices vacías y matrices inicializadas para mostrar el tablero y la ayuda
# ayuda=[]
# tablero=[]
# auxiliar=["-","-","-"]
# aux_ayuda=["", "", ""]
# #lista con los números disponibles para ingresar en el juego
# #los valores se cooresponden con las posiciones en el tablero
# disponibles=[0, 1, 2, 10, 11, 12, 20, 21, 22]
# #variables a utilizar en el juego
# jugada_actual=999
# indice_fila=999
# indice_columna=999
# jugador=""
#
# #carga el tablero con los valores iniciales "-"
# for i in range(3):
#     tablero.append(auxiliar)
#
# #carga la ayuda con las posiciones y los números que corresponde ingresar
# for i in range(3):
#     for j in range(3):
#         aux_ayuda[j]= str(i)+str(j)
#     ayuda.append(aux_ayuda)
#     aux_ayuda=["", "", ""]
#
# #Variables buleanas para verificar si hay TA TE TI
# fila0= (tablero[0][0] == tablero[0][1]) and (tablero[0][0] == tablero[0][2]) and (tablero[0][0] != "-")
# fila1= (tablero[1][0] == tablero[1][1]) and (tablero[1][0] == tablero[1][2]) and (tablero[1][0] != "-")
# fila2= (tablero[2][0] == tablero[2][1]) and (tablero[2][0] == tablero[2][2]) and (tablero[2][0] != "-")
# columna0= (tablero[0][0] == tablero[1][0]) and (tablero[0][0] == tablero[2][0]) and (tablero[0][0] != "-")
# columna1= (tablero[0][1] == tablero[1][1]) and (tablero[0][1] == tablero[2][1]) and (tablero[0][1] != "-")
# columna2= (tablero[0][2] == tablero[1][2]) and (tablero[0][2] == tablero[2][2]) and (tablero[0][2] != "-")
# d_mayor= (tablero[0][0] == tablero[1][1]) and (tablero[0][0] == tablero[2][2]) and (tablero[0][0] != "-")
# d_menor= (tablero[0][2] == tablero[1][1]) and (tablero[0][2] == tablero[2][0]) and (tablero[0][2] != "-")
# terminado= fila0 or fila1 or fila2 or columna0 or columna1 or columna2 or d_mayor or d_menor
#
# print()
# #imprime el tablero vacío
# print("= TABLERO =")
# for i in range(3):
#     print("", end=" ")
#     for j in range(3):
#         print(tablero[i][j], end= "   ")
#     print()
# print()
#
# #imprime la ayuda
# print("== AYUDA ==")
# for i in range(3):
#     for j in range(3):
#         print(ayuda[i][j], end= "  ")
#     print()
# print()
#
# #inicio del juego
# #se desarrolla dentro de un bucle for (máximo 9 intentos si no hay ganador)
# for intento in range(9):
#     #variables del juego que almacenarán la posición y el jugador (alternando entre X y 0)
#     indice_fila=999
#     indice_columna=999
#     jugador=""
#     #variables auxiliares para cargar nuevamente el tablero modificado
#     tablero_aux=[]
#     aux=[]
#     elemento="  "
#
#     #Imprime la lista de números disponibles
#     print(disponibles)
#     #solicita se ingrese un número de la lista y 
#     # continúa en un while hasta que el valor es correcto
#     jugada_actual = int(input("Ingrese un número de la lista: "))
#     while jugada_actual not in disponibles:
#         print("Opción incorrecta.")
#         jugada_actual = int(input("Ingrese un número de la lista: "))
#
#     # en indice_fila almacena la fila que corresponde al 
#     # número ingresado (usa división entera)
#     # en indice_columna almacena la columna (usa el resto de la división)
#     indice_fila= jugada_actual//10
#     indice_columna= jugada_actual%10
#
#     #En cada vuelta del bucle alterna del jugador X al O 
#     # (utiliza el resto de dividir por 2)
#     if intento%2 == 0:
#         jugador= "X"
#     else:
#         jugador= "0"
#
#     #En una lista auxiliar carga los valores actuales del tablero, 
#     # pero en la posición indicada por indece_fila e indice_columna 
#     # carga una X o una 0 de acuerdo al jugador de ese turno
#     for k in range(3):
#         for l in range(3):
#             if (k == indice_fila) and (l == indice_columna):
#                
#                 tablero_aux.append(jugador)
#             else:
#                 tablero_aux.append(tablero[k][l])
#
#     #limpia el tablero para cargarle los valores con las modificaciones
#     tablero.clear()
#
#     #recorre la lista auxiliar y guarda de a cada 3 valores en una lista (fila)
#     #  que se agregá al nuevo tablero
#     for j in range(3):
#         aux=[]
#         for i in range(3):
#             aux.append(tablero_aux[i+j*3])
#         tablero.append(aux)
#       
#     #remueve el valor de la posición utilizada de la lista disponibles
#     disponibles.remove(jugada_actual)
#
#     #limpia las variables auxiliares
#     jugada_actual=999
#     indice_fila=999
#     indice_columna=999
#
#     #Variables buleanas para verificar si hay TA TE TI
#     fila0= (tablero[0][0] == tablero[0][1]) and (tablero[0][0] == tablero[0][2]) and (tablero[0][0] != "-")
#     fila1= (tablero[1][0] == tablero[1][1]) and (tablero[1][0] == tablero[1][2]) and (tablero[1][0] != "-")
#     fila2= (tablero[2][0] == tablero[2][1]) and (tablero[2][0] == tablero[2][2]) and (tablero[2][0] != "-")
#     columna0= (tablero[0][0] == tablero[1][0]) and (tablero[0][0] == tablero[2][0]) and (tablero[0][0] != "-")
#     columna1= (tablero[0][1] == tablero[1][1]) and (tablero[0][1] == tablero[2][1]) and (tablero[0][1] != "-")
#     columna2= (tablero[0][2] == tablero[1][2]) and (tablero[0][2] == tablero[2][2]) and (tablero[0][2] != "-")
#     d_mayor= (tablero[0][0] == tablero[1][1]) and (tablero[0][0] == tablero[2][2]) and (tablero[0][0] != "-")
#     d_menor= (tablero[0][2] == tablero[1][1]) and (tablero[0][2] == tablero[2][0]) and (tablero[0][2] != "-")
#     terminado= fila0 or fila1 or fila2 or columna0 or columna1 or columna2 or d_mayor or d_menor
#
#     print()
#     #imprime nuevamente el tablero (ya modificado) y la ayuda
#     print("= TABLERO =")
#     for i in range(3):
#         print("", end=" ")
#         for j in range(3):
#            
#             print(tablero[i][j], end= "   ")
#         print()
#     print()
#
#     print("== AYUDA ==")
#     for i in range(3):
#         for j in range(3):
#             print(ayuda[i][j], end= "  ")
#         print()
#     print()
#
#     #si la comprobación lógica es True el juego está terminado 
#     # porque un jugador ganó el juego y no completa el for (sale por el break)
#     if terminado:
#         print("Felicitaciones!! Usted ha ganado el TA TE TI")
#         break
#
# #si no hubo ganadores sale al finalizar el for e indica que el juego ha terminado
# print("Juego terminado")
# print()


# Ejercicio 10
""" 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
• Mostrar el total vendido por cada producto. 
• Mostrar el día con mayores ventas totales. 
• Indicar cuál fue el producto más vendido en la semana. """

# #dias_semana y productos son auxiliares para solicitar los datos al usuario
# dias_semana=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
# productos=["pantalón", "camisa", "remera", "campera"]
# #matriz auxiliar para cargar las ventas diarias
# aux_ventas=[0, 0, 0, 0]
# #matriz principal de ventas
# matriz_ventas = []
# #variables auxiliares 
# suma=0
# maximo_semana=0
# dia_maximo=""
# maximo_producto=0
# mas_vendido=""
#
# print()
# #carga los valores diarios de cada producto con un for (los valores son float)
# for dia in dias_semana:
#     for i in range(len(productos)):
#         aux_ventas[i]= float(input(f"Ingrese las ventas en pesos del producto {productos[i]} del día {dia}: "))
#     matriz_ventas.append(aux_ventas)
#     aux_ventas=[0, 0, 0, 0]
#
# print()
# #muestra la matriz
# for i in range(len(dias_semana)):
#     for j in range(len(productos)):
#         if j < (len(productos)-1):
#             print(f"{matriz_ventas[i][j]}", end= " - ")
#         else:
#             print(f"{matriz_ventas[i][j]}")
# print()
#
# #recorre las columnas de la matríz acumulando en suma cada producto
# for j in range(len(productos)):
#     suma=0
#     for i in range(len (dias_semana)):
#         suma += matriz_ventas[i][j]
#   
#     #guarda en maximo_producto el valor del mayor    
#     if maximo_producto < suma:
#         maximo_producto = suma
#         mas_vendido = productos[j]
#     #muestra las ventas por producto
#     print(f"El total vendido del producto {productos[j]} es {suma} pesos")
# print()
# #muestra el producto más vendido
# print(f"El producto más vendido es {mas_vendido} con {maximo_producto} pesos")
#
# #recorre las filas de la matriz acumulando en suma el total del día
# #si es el mayor queda guardado en maximo_semana y el nombre del día en dia_máximo
# for i in range(len(dias_semana)):
#     suma=0
#     for j in range(len (productos)):
#         suma += matriz_ventas[i][j]
#  
#         if maximo_semana < suma:
#             maximo_semana = suma
#             dia_maximo = dias_semana[i]
# print()
# print(f"El día de mayor venta en la semana es el {dia_maximo} con {maximo_semana} pesos")
# print()


