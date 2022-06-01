# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 12:38:24 2022

@author: ricardo
Programa 1. Iniciando con python ciclos
"""
#----------------------------------------------------------
#Manera 1

# entrada = ""
# suma = 0
# while suma < 3 and entrada != "bye":
#     entrada = input("Clave: ")
#     suma += 1
#     print("Intento %d " % suma)
# print ("Utilizaste %d intentos" % suma)
#-----------------------------------------------------------
#Manera 2

# entrada = ""
# suma = 0
# fallido = 0
# while suma < 3:
#     suma += 1
#     print("Intento %d " % suma)
#     entrada = input("Clave: ")
#     print()
#     #Al ingresar "bye", se evita que 
#     #la variable fallido se incremente
#     if entrada == "bye":
#         continue
#     fallido += 1
# print("Tuviste %d intentos fallidos." % fallido)
#-----------------------------------------------------------
#Manera 3

# suma = 0
# while suma < 3:
#     entrada = input("Clave:")
#     #Si se ingresa la palabra "bye",
#     #se termina el ciclo
#     if entrada == "bye":
#         break
#     suma = suma + 1
#     print("Intento %d. \n " % suma)
# print("Tuviste %d intentos fallidos." % suma)
#------------------------------------------------------------