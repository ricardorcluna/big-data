# -*- coding: utf-8 -*-
"""
@author: ricardo
"""

#------------------------------------------------------------------------------

# a) Crear una lista de, al menos, 20 elementos 
#     (agregue algunos elementos duplicados). Realice las siguientes actividades:
#  * Sume todos los elementos de una lista
#  * Multiplique todos los elementos de una lista
#  * Determine el menor y el mayor de los elementos de la lista
#  * Realice una copia de la lista y elimine elementos repetidos
#  * A partir de la siguiente lista ['G', 'N'] concatene con otra lista de números 
#      [1,.., N] donde N es dado por el usuario o predefinido. Si N = 4, 
#      la salida sería : ['G1', 'N1', 'G2', 'N2',  'G3', 'N3', 'G4', 'N4'] 

# # Se crean las listas de forma predifinida
# Lista_A = [3, 6, 7, 10, 1, 6, 17, 8, 6, 2, 4, 20, 5, 9, 1, 22, 1, 4, 14, 24]
# Lista1_A = ['G', 'N']
# Lista2_A = [1,2,3,4]

# # Se guarda todo el proceso en una funciona mas por gusto que por funcionalidad
# def incisoA (Lista, Lista1, Lista2):
    
#     #Se crean variables con valores asignados y otros sin valores
#     Suma = 0    # La variable suma se le puede asignar 
#     Mult = 1     # Mientras que en la variable mult no se puede hacer eso
#     Menor = Lista[1]    # Se asigna el primer valor de la lista para evaluar con los otros valores
#     Mayor = Lista[1]    # Se asigna el primer valor de la lista para evaluar con los otros valores
#     ListaR_A = []   
    
#     # Se usara un for que tomara para la secuencia una lista (Lista_A)
#     for numero in Lista:
        
#         Suma += numero # Se sumara cada valor de la lista en la variable Suma
#         Mult *= numero # Se multiplicara cada valor de la lista en la variable Mult
        
#         # Se analiza si el valor de la actual iteracion es mayor o menor al Mayor y Menor
#         if ( numero < Menor ) : Menor = numero
#         if ( numero > Mayor ) : Mayor = numero
    
#     # Se utiliza dos for donde el primero es con Lista2 ya que este tiene mas valores en la lista
#     for numero in Lista2:
#         for letra in Lista1:
#             # Se agrega un valor a la lista con append
#             # Se convierte numero en un String para asi concatenar los dos valores
#             ListaR_A.append( letra + str(numero) )

#     # Se muestran los variables
#     print ("Suma de la lista =", Suma )
#     print ("Multriplicación de la lista =", Mult )
#     print ("Menor de la lista =", Menor )
#     print ("Mayor de la lista =", Mayor)
#     print ( ListaR_A )

# # Se llama la funcion con parametros
# incisoA (Lista_A, Lista1_A, Lista2_A)

#------------------------------------------------------------------------------

# b) Convertir una lista  a una lista de diccionarios.
#     [1,2,3,4,5,6]  ["Luis", "Paco", "Hugo", "Daisy", "Mimi", "Donald"]

#     La salida del programa sería :  
#         [{numero : 1, nombre:"Luis"}, {numero:2, nombre:"Paco"}, 
#           {numero:3, nombre:"Hugo"}, {numero:4, nombre:"Daisy"}, 
#           {numero:5, nombre:"Mimi"}, {numero:6, nombre:"Donald"}]

# # Se crean listas con valores predifinidas    
# Lista1B = [1,2,3,4,5,6]
# Lista2B = ["Luis", "Paco", "Hugo", "Daisy", "Mimi", "Donald"]
# Lista_B = []
 
# # Se utiliza el zip para hacer agrupar multiples iteraciones
# # Se puede utilizar zip ya que las dos listas comparte el mismo numero de valores
# # Si no es asi zip haria que la cantidad de iteraciones sea igual al menor numero
# for i, j in zip(Lista1B, Lista2B):
        
#         # Dentro del for se crea un diccionario
#         dicc = {'numero': i, 'nombre': j} 
#         # Despues utilizando append para agregar el diccionario dentro de la lista
#         Lista_B.append(dicc)

# # Se imprime la lista
# print( Lista_B )

#------------------------------------------------------------------------------
    
# c) Extraer los elementos de una lista de tuplas. Por ejemplo:
#   [("Luis", 100, 100), ("Paco", 89, 95), 
#       ("Hugo", 65, 98), ("Donald", 45, 70), ("Daisy", 90, 96)]

#   La salida del programa sería:
# ["Luis", "Paco", "Hugo", "Donald", "Daisy"]  
# [100, 89, 65, 45, 90]
# [100, 95, 98, 70, 96]

# # Se crea una lista predefinida
# Lista_C = [("Luis", 100, 100), ("Paco", 89, 95), 
#             ("Hugo", 65, 98), ("Donald", 45, 70), 
#             ("Daisy", 90, 96)]

# # Se creo una funcion solo por gusto y comodidad
# def incisoC (Lista):
    
#     # Se crean 3 Listas vacias
#     lista1 = []
#     lista2 = []
#     lista3 = []

#     # Utilizando for con la secuencia de lo que nos devuelve list en Lista_C
#     # Para asi acceder a las tuplas internas de la Lista_C
#     for tupla in list(Lista_C):
        
#         # Se agregan los valores en cada diferente lista con la ayuda append 
#         lista1.append(tupla[0]) 
#         lista2.append(tupla[1])
#         lista3.append(tupla[2])

#     # Se imprimen las Listas
#     print(lista1)
#     print(lista2)
#     print(lista3)
    
# # Se llama a la funcion y este recibe como parametro a Lista_C
# incisoC(Lista_C)


#------------------------------------------------------------------------------

# d) Crear tres diccionarios que contengan 
# numero de control (llave) y nombre (valor). 
# Y convertirlos a un sólo diccionario.

#         diccUno = {1: "Luis", 2: "Paco"}
#         diccDos = {3: "Hugo", 4: "Donald"}
#         diccTres = {5: "Daisy", 6: "Mimi"}
#         resultado = 
#           {1: "Luis", 2: "Paco", 3: "Hugo", 4: "Donald", 5: "Daisy", 6: "Mimi"}

# Se crean 3 diccionarios con valores predifinidos
diccUno = {1: "Luis", 2: "Paco"}
diccDos = {3: "Hugo", 4: "Donald"}
diccTres = {5: "Daisy", 6: "Mimi"}

# Despues se aprovechan los metodos del diccionario copy y update
dicc4 = diccUno.copy() # Donde se copia el diccionario 1 en el 4
dicc4.update(diccDos) # Para despues 'actualizar' o añadir los valores del diccionario 2 al 4 
dicc4.update(diccTres) # Y esto se aplica de nuevo con el diccionario 3

# Para al final imprimir el diccionario 4 para mostrar el resultado
print(dicc4)
