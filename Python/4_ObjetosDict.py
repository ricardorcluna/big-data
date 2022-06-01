# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:42:15 2022

@author: ricardo
Programa 4. Objectos Dict
"""
#forma 1
# persona = {"nombre":"José", "apellido_1": "Pérez",
#            "apellido_2": "López"}
# print(persona)
# print(persona["apellido_2"])
# persona['nombre'] = "Luis"
# print(persona)

# #forma 2
# otra = dict(nombre = "Armando", 
#             escolaridad_máxima="Licenciatura")
# print(otra)
# del otra['nombre']
# print(otra)
# #-------------------------------------------------------
# #Primera forma
# persona = {"nombre":"José", "apellido_1": "Pérez",
#             "apellido_2": "López"}
# print(persona.get("nombre"))
# persona.update({"nombre":"Pedro",
#                 "codigo_postal":"27000"})
# print(persona)
# persona.update({"profesion": "ISC"})
# print(persona)
# persona.setdefault("email", "correo_isc@itlaLaguna.edu.mx")
# print(persona)
# persona.setdefault("certificacion")
# print(persona)
# elementos = persona.items() #objeto iterable
# print(elementos)
# for elemento in elementos:
#     print(elemento)
    
# llaves = persona.keys() #objeto iterable
# print(llaves)
# for clave in llaves:
#     print(clave)
    
# valores = persona.values() #objeto iterable
# print(valores)
# for val in valores:
#     print(val)
