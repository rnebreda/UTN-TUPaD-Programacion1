"""Utilería de funciones para manejo de archivos"""

#Imprime los elementos de un archivo con el formato solicitado
def imprimir(archivo_a_leer):
    with open(archivo_a_leer,"r") as archivo:

        lineas = archivo.readlines()
            
        for linea in lineas:

            partes = linea.strip().split(",")

            print("Producto: ", end=" ")

            for i in range (len(partes)):

                if i != len(partes)-1:
                    print (f"{partes[i]}", end= " | ")
                else:
                    print (f"{partes[i]}")
        print()

#Agrega al archivo un nuevo elemento en una nueva linea
#El elemento es ingresado por el usuario
def agregar(archivo_a_modificar):
    with open(archivo_a_modificar, "a") as archivo:

        nombre= input("Ingrese el nombre del producto: ")
        precio= input("Ingrese el valor en pesos: ")
        cantidad= input("Ingrese la cantidad en stock: ")

        archivo.write(f"{nombre},${precio},{cantidad}\n")
    print()

#Agrega los elementos del archivo a una lista como dicionarios
def lineas_diccionario (archivo_a_leer,lista):
    with open(archivo_a_leer,"r") as archivo:

        lineas = archivo.readlines()
            
        for linea in lineas:

            partes = linea.strip().split(",")

            lista.append({"nombre": partes[0],"precio": partes[1],"cantidad":partes[2]})


#Busca un elemento en la lista de diccionarios por la clave "nombre"
def buscar_por_nombre(lista, nombre):

    encontrado= False

    for elemento in lista:

        #Si lo encuentra lo imprime con el formato solicitado y sale del for
        if elemento["nombre"]== nombre:
            print(f"Producto: {elemento["nombre"]} | {elemento["precio"]} | {elemento["cantidad"]}")
            encontrado=True
            break
    
    #Si no lo encuentra muestra un mensaje de error
    if not encontrado:
        print(f"El elemento {nombre} no se encuentra en el catálogo")


#Actualiza los elementos en el archivo desde una lista de diccionarios (sobreescribe)
def actualizar(archivo_a_actualizar, lista):

    with open(archivo_a_actualizar, "w") as archivo:

        for elemento in lista:
            archivo.write(f"{elemento["nombre"]},{elemento["precio"]},{elemento["cantidad"]}\n")


#Agrega un elemento nuevo a la lista (sin actualizar en el archivo)
def agregar_en_lista(lista):
            
    nombre= input("Ingrese el nombre del producto que desea agragar: ")
    precio= "$" + input("Ingrese el valor en pesos: ")
    cantidad= input("Ingrese la cantidad en stock: ")

    lista.append({"nombre": nombre,"precio": precio,"cantidad": cantidad})
    print(f"Se ha agregado {nombre} a la lista")
    print()
    