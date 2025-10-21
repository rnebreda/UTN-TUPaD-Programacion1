""" Práctico 8: Manejo de Archivos
Rolando Nebreda 18.350.686 """

#Utiliza una utilería de funciones existe en utils
import utils

#Ejercicio 1
""" 1) Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad """

# with open("productos.txt", "w") as productos:
#     productos.write("Teclado,$100.3,15\n")
#     productos.write("Monitor,$500.8,10\n")
#     productos.write("Mouse,$20.6,12\n")


#Ejercicio 2
""" 2) Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30 """

# with open("productos.txt","r") as productos:

#     lineas = productos.readlines()
        
#     for linea in lineas:

#         partes = linea.strip().split(",")

#         print("Producto: ", end=" ")

#         for i in range (len(partes)):

#             if i != len(partes)-1:
#                 print (f"{partes[i]}", end= " | ")
#             else:
#                 print (f"{partes[i]}")
#     print()


# Ejercicio 3
"""3) Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente. """

# utils.imprimir("productos.txt")

# utils.agregar("productos.txt")

# utils.imprimir("productos.txt")


# Ejercicio 4
""" 4) Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad. """

# productos=[]
# utils.lineas_diccionario("productos.txt", productos)
# print(productos)
# print()

# Ejercicio 5
""" 5) Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.  """

# productos=[]
# utils.lineas_diccionario("productos.txt", productos)

# nombre_buscado= input("Ingrese el nombre del producto buscado: ")
# utils.buscar_por_nombre(productos, nombre_buscado)


# Ejercicio 6
""" 6) Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.  """

# #Imprime elementos en el archivo
# utils.imprimir("productos.txt")

# #Crea una lista vacía, y le carga los datos del archivo como diccionarios
# productos=[]
# utils.lineas_diccionario("productos.txt", productos)

# #Agrega un elemento nuevo a la lista
# utils.agregar_en_lista(productos)

# #Actualiza el archivo
# utils.actualizar("productos.txt", productos)

# #Imprime elementos del archivo con el elemento agregado
# utils.imprimir("productos.txt")


