""" Práctico 7: Estructuras de datos complejas
Rolando Nebreda 18.350.686 """

#Ejercicio 1
""" 1) Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
Añadir las siguientes frutas con sus respectivos precios: 
● Naranja = 1200 
● Manzana = 1500 
● Pera = 2300   """

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# print(precios_frutas)

# precios_frutas["Naranja"]= 1200
# precios_frutas["Manzana"]= 1500
# precios_frutas["Pera"]= 2300

# print(precios_frutas)

#Ejercicio 2
""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800   """


# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# print(precios_frutas)

# precios_frutas["Banana"]= 1330
# precios_frutas["Manzana"]= 1700
# precios_frutas["Melón"]= 2800

# print(precios_frutas)


# Ejercicio 3
"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios.  """

# precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

# print(precios_frutas)

# frutas = list (precios_frutas.keys())

# print (frutas)


# Ejercicio 4
""" 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe. """

# #Crea el diccionario vacío
# contactos = {}
# #Cantidad de contactos a cargar en el diccionario
# CANTIDAD = 5

# #función para agregar un nuevo contacto al diccionario
# def cargar_contacto():
#     clave= input("Ingrese el nombre del nuevo contacto: ")
#     valor= input("Ingrese el número telefónico: ")
#     contactos[clave]=valor

# #función para buscar un contacto en el diccionario e imprime su nombre y número telefónico
# def buscar_numero_por_contacto():
#     clave= input("Ingrese el nombre del contacto buscado: ")
#     valor= contactos.get(clave)
#     if valor == None:
#         print ("El contacto buscado no existe")
#     else:
#         print(f"El número telefónico de {clave} es {valor}")

# #Carga la cantdad de contactos deseada.
# #Si el contacto ya existe no lo carga y queda el diccionario con un elemento menos de la cantidad deseada.
# for i in range(CANTIDAD):
#     cargar_contacto()

# #Imprime el diccionario (no necesario)
# print(contactos)
# print()

# #Busca en el diccionario un contacto
# buscar_numero_por_contacto()


# Ejercicio 5
""" 5) Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra.   """

# #función para obtener las palabras únicas de una frase (usando set)
# def separar_en_palabras(frase):
#     #crea un conjunto vacío
#     palabras = set()
#     #carga las palabras de la frase en el set utilizando la función update()
#     #por separado (usando la función split()), y eliminando puntos y comas (usando la función replacce()).
#     # Si ya existe en el set no la repite.
#     palabras.update(frase.lower().replace(",", "").replace(".", "").split())
#     #Imprime los elementos del set
#     print(palabras)

# #funcion para obtener las palabras de una frase y la cantidad de veces que se repiten (usando diccionario)
# def cuenta_palabras_en_frase(frase):
#     #crea un diccionario vacío
#     palabras = {}
#     #carga las palabras de la frase en una lista por separado (usando la función split()), 
#     #y eliminando puntos y comas (usando la función replacce()).
#     lista_palabras= frase.lower().replace(",", "").replace(".", "").split()
#     #variable para contar las repeticiones
#     cuenta_palabras= 0
    
#     #recorre la lista con un for
#     for palabra in lista_palabras:

#         #para cada palabra en la lista cuenta las repeticiones (usando la función count())
#         cuenta_palabras= lista_palabras.count(palabra)
#         #carga la palabra como clave y la cantidad de repeticiones en el diccionario
#         #Si ya existe, no lo agrega.
#         palabras[palabra]=cuenta_palabras

#     #Imprime los elementos del diccionario
#     print(palabras)

# frase= input("Ingrese una frase: ")

# separar_en_palabras(frase)
# print()

# cuenta_palabras_en_frase(frase)


# Ejercicio 6
""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno.  """

# #diccionario vacío
# notas={}

# #funcion que retorna una tupla con las 3 notas de un alumno
# def carga_notas(nombre):

#     notas=[]
#     nota= 0

#     #en un for pide al usuario que ingrese las 3 notas y las agrega a una lista
#     for i in range(3):
#         #cada nota es un entero (sin validar)
#         nota= int(input(f"Ingrese la nota {i+1} del alumno {nombre}: "))
#         notas.append(nota)
#     print()

#     #la funcion retorna una tupla con 3 valores enteros
#     return notas[0], notas[1], notas[2]

# #función que solicita nombre y notas del alumno y los agrega a un diccionario (alumno: tupla)
# #si el alumno ya existe lo modifica. Utiliza la función carga_notas()
# def alumno_notas():

#     for i in range(3):

#         alumno= input("ingrese el nombre del alumno: ")

#         notas[alumno]= carga_notas(alumno)

# #función que obtiene el promedio de los valores de una tupla
# #(valores numéricos sin validar)
# def promedio(notas):
#     suma= 0

#     for i in range(len(notas)):
#         suma += notas[i]

#     #retorna el promedio de los valores (no importa cuantos)
#     return suma/len(notas)

# #función que muestra los alumnos y sus promedios
# def muestra_promedios():

#     #recorre el diccionario y para cada alumno (clave), muestra su promedio redondeado a 2 decimales
#     for clave, valor in notas.items():
#         print(f"El promedio de {clave} es {round(promedio(valor), 2)}")
#     print()

# #ejecuta la carga de datos
# alumno_notas()

# #muestra los alumnos y sus promedios
# muestra_promedios()


# Ejercicio 7
"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2: 
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).  """

# #Conjunto de estudiantes que aprobaron Parcial 1
# estudiantes1={"Ana", "Juan", "Pedro", "Carolina", "Lucas", "Candela", "Gabriela", "Pablo", "Daniel", "Noelia"}
# #Conjunto de estudiantes que aprobaron Parcial 2
# estudiantes2={"Pedro", "Candela", "Daniel", "Alejandro", "Silvana", "Emilio", "Yanina", "Belén"}

# print("Estudiantes que aprobaron ambos parciales")
# ambos= set(estudiantes1 & estudiantes2)
# print(ambos)
# print()

# print("Estudiantes que aprobaron un solo parcial de los dos")
# solo_uno= set(estudiantes1.symmetric_difference(estudiantes2))
# print(solo_uno)
# print()

# print("Estudiantes que aprobaron al menos un parcial")
# todos= set(estudiantes1 | estudiantes2)
# print(todos)
# print()


# Ejercicio 8
""" 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe.   """

# #Diccionario de productos
# stock_productos= {"manteca":10, "leche":6, "huevos":12, "queso": 5, "aceite":4}

# #función para consultar el stock de un producto dado
# def consultar_stock(producto):

#     if producto in stock_productos:
#         print(f"El stock actual de {producto} es {stock_productos[producto]}")
    
#     else:
#         print(f"El producto {producto} no existe en el catálogo")

# #función para agregar unidades al stock de un producto
# #ingresa un entero (sin validar)
# def agregar_unidades(producto):

#     if producto in stock_productos:
#         cantidad_a_agregar_a_stock= int(input(f"Ingrese la cantidad de unidades a agregar al stock: "))
#         stock_productos[producto] += cantidad_a_agregar_a_stock
#         print(f"El stock actual de {producto} es {stock_productos[producto]}")
    
#     else:
#         print(f"El producto {producto} no existe en el catálogo")

# #función para agregar un producto nuevo al catálogo
# #ingresa con valor de stock cero
# def agregar_producto(producto):

#     if producto not in stock_productos:
#         stock_productos[producto] = 0
#         print(f"El producto {producto} se ha agregado con éxito")
    
#     else:
#         print(f"El producto {producto} ya existe en el catálogo")

# #Imprime la lista de productos (solo la clave)
# print(list(stock_productos))

# #Solicita un producto para consultar stock
# producto = input("ingrese un producto para consultar su stock: ")
# consultar_stock(producto)
# print()

# #Solicita un producto para agrgar unidades al stock
# print(stock_productos)
# producto = input("ingrese un producto para agregar unidades a su stock: ")
# agregar_unidades(producto)
# print(stock_productos)
# print()

# #Solicita un producto para agregar al catálogo
# producto = input("ingrese un producto para agregar al catálogo: ")
# agregar_producto(producto)
# print(stock_productos)
# print()

# Ejercicio 9
""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.   """

# #Genera un diccionario en el cual la clave es una tupla (día, hora) y el valor es un evento programado.
# agenda={("lunes", "08:00"): "Reunión diaria", ("lunes", "10:00"): "Logística", ("lunes", "12:00"): "Almuerzo", ("lunes", "14:00"): "Recepción de MP", ("lunes", "16:00"): "Revisión Compras", \
#         ("martes", "08:00"): "Reunión diaria", ("martes", "10:00"): "Producción", ("martes", "12:00"): "Almuerzo", ("martes", "14:00"): "", ("martes", "16:00"): "Revisión Seguridad", \
#         ("miercoles", "08:00"): "Reunión diaria", ("miercoles", "10:00"): "Laboratorio", ("miercoles", "12:00"): "Almuerzo", ("miercoles", "14:00"): "Revisión Depósitos", ("miercoles", "16:00"): "", \
#         ("jueves", "08:00"): "Reunión diaria", ("jueves", "10:00"): "Calidad de Producto", ("jueves", "12:00"): "Almuerzo", ("jueves", "14:00"): "", ("jueves", "16:00"): "Revisión RRHH", \
#         ("viernes", "08:00"): "Reunión diaria", ("viernes", "10:00"): "Planeamiento", ("viernes", "12:00"): "Almuerzo", ("viernes", "14:00"): "Resumen semanal Gerencia", ("viernes", "16:00"): ""}

# #Lista auxiliar para validar días al ser ingresado por el usuario.
# dias_semana={"lunes", "martes", "miercoles", "jueves", "viernes"}

# #función para consultar la agenda de un día dado
# #Si el día no está en la lista de días de la semana, avisa que el dato es incorrecto y no ejecuta
# def consulta_por_dia(dia):

#     encontrado= False

#     if dia in dias_semana:


#         for clave, valor in agenda.items():
            
#             #Imprime todos los datos de la agenda que coinciden con el día buscado
#             if clave[0] == dia:
#                 print(f"{clave[0]} {clave[1]} : {valor}")
        
#         encontrado= True

#     if not encontrado:
#         print("El valor ingresado es incorrecto")

# #función para consultar la agenda de un día y horario dado
# #Si el día no está en la lista de días de la semana, avisa que el dato es incorrecto y no ejecuta
# #Ídem si no existe un horario para el día buscado.
# #Si encuentra el día y horario y está vacío, avisa que en ese horario no tiene eventos programados
# #Si lo encuentra y no está vacío lo imprime.
# def consulta_por_dia_hora(dia, hora):

#     encontrado= False

#     if dia in dias_semana:

#         for clave, valor in agenda.items():
        
#             if clave[0] == dia and clave[1] == hora:
#                 if valor != "":
#                     print(f"{clave[0]} {clave[1]} : {valor}")

#                 else:
#                     print(f"No tiene eventos programados el día {clave[0]} a esa hora")
                
#                 #Si lo encuentra deja de iterar luego de imprimir o mostrar mensaje
#                 encontrado = True
#                 break

#     if not encontrado:
#         print("El valor ingresado es incorrecto")

# #función para imprimir la agenda completa
# def imprimir_agenda():
#     auxiliar=""
#     print()
#     print("****AGENDA****")
#     for clave, valor in agenda.items():

#         if clave[0] != auxiliar:
#             print()
#             print(clave[0])
                
#         print(f"{clave[1]} : {valor}")
#         auxiliar=clave[0] 
    
#     print()

# #Imprime la agenda completa
# imprimir_agenda()

# #Imprime todos los eventos programados de un día dado
# dia= input("Ingrese un día para consultar su agenda: ")

# consulta_por_dia(dia)
# print()

# #Imprime el evento programado de un día y horario dado
# dia= input("Ingrese un día para consultar su agenda: ")

# #Si ya el día ingresado no es correcto, no se ejecuta y muestra un mensaje
# if dia in dias_semana:
#     hora= input(f"Ingrese una hora para consultar su agenda para el día {dia}: ")
#     consulta_por_dia_hora(dia, hora)

# else:
#     print("El valor ingresado es incorrecto")

# print()


# Ejercicio 10
""" 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores.   """

# #diccionario de paises (clave) y capitales (valor)
# paises_capitales= {"Francia" : "Paris", "Inglaterra" : "Londres", "España" : "Madrid", "Alemania" : "Berlin", "Italia" : "Roma"}

# #diccionario vacío de capitales (clave) y paises (valor)
# capitales_paises = {}

# #imprime antes
# print("Paises y sus capitales")
# print(paises_capitales)
# print()

# #utiliza un for para recorrer el diccionario e intercambiar las claves y valores, agregandolos en el segundo diccionario
# for clave, valor in paises_capitales.items():
#     capitales_paises[valor]= clave

# #imprime después
# print("Capitales y sus paises")
# print(capitales_paises)

