# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:48:33 2022

@author: ricardo
Programa 6. Funciones
"""

# def saludo():
#     print("Hola desde la funcion")
# #Programacion principal
# saludo()

# def suma(primero, segundo):
#     '''Despliega la suma de dos objetos'''
#     print(primero + segundo)
    
# suma(5, 10)

# #Tupla se envía con asterisco
# def promedio(*muestras):
#     '''Calcula el promedio de la muestra correspondiente'''
#     promedio = sum(muestras)/len(muestras)
#     print('El promedio de la muestra de %d elementos es %.3f.'
#           %(len(muestras), promedio))

# promedio(1, 3, 5, 8, 11, 24, 90, 29)
# promedio(14, 38, 1)


# def promedio(titulo, *muestras):
#     '''Calcula el promedio de la muestra correspondiente
#        del primero, el cual será utilizado como título.'''
#     promedio = sum(muestras)/len(muestras)
#     print(titulo)
#     print('El promedio de la muestra de %d elementos es %.3f.'
#           %(len(muestras), promedio))
    
# promedio('Conteo de abejas en campo.', 34, 45, 61, 23, 47, 41, 52)
    
# # objeto dict doble asterisco
# def superficie(**dato):
#     '''Calcula la superficie de una figura geométrica si 
#        los parámetros ingresados coinciden'''
#     superficie = 0
#     if dato["tipo"] == "Rectángulo":
#         superficie = float(dato["base"]) * float(dato["altura"])
#     elif dato["tipo"] == "Triángulo":
#         superficie = float(dato["base"]) * float(dato["altura"]) / 2
#     elif dato["tipo"] == "Círculo":
#         superficie = float(dato["radio"]) ** 2 * 3.1416
#     else:
#         print("No puedo calcular la superficie.")
#     if superficie != 0:
#         print("La superficie del %s es de %.2f"
#               % (dato["tipo"].lower(), superficie))

# superficie(base=22.0, altura=30, tipo = "Rectángulo")

# #return
# def promedio(*muestras):
#     return (len(muestras), sum(muestras) / len(muestras))

# media = promedio(1, 3, 5, 8, 11, 24, 90, 29)
# print('El promedio de la muestra de %d elementos es %.3f.' %(media))

# #funciones anidadas
# def lista_primos(limite):
#     '''Genera una lista de los números primos comprendidos entre'''
#     #la lista inicia con el número 2
#     lista = [2]
    
#     def esprimo(numero):
#         '''Valida si numero es divisible entre algún
#         elemento de lista. De ocurrir, 
#         regresa False. De lo contrario, regresa True'''
#         for primo in lista:
#             if numero % primo == 0:
#                 return False
#         return True
#     for numero in range(3, limite + 1):
#         #Si esprimo(numero) regresa True, añade el valor de
#         #de numero a lista
#         if esprimo(numero):
#             lista.append(numero)
#         return lista
    
# print(lista_primos(200))


# def factorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         fact = numero * factorial(numero-1)
#         return fact
    
# print(factorial(4))

# #Tarea:
# #manejo de excepciones, funciones de orden superior
# #y decoradores. Qué es, como se programa, ejemplos

# #Funciones Lambda o anónimas
# #Sintáxis: lambda<argumentos>:<código>
# saluda = lambda texto='mundo', ancho=50: print('Hola, {}.'.format(texto).center(ancho))
# saluda()
# saluda('mundi', 20)
# #Función Lambda con condicional
# #Sintáxis: Lambda <argumentos>: <expresion_1> if <condicion> else <expresión_2>
# es_par = lambda numero: True if numero % 2 == 0 else False
# print(es_par(4))
# factorial = lambda numero: numero * factorial(numero - 1) if numero > 1 else 1 
# print(factorial(5))
