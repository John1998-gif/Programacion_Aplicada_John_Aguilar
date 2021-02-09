# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:23:26 2020

@author: john
"""


nombre=input("Ingrese su primer nombre\n")
segun_nombre=input("Ingrese su segundo nombre\n")
apellido=input("Ingrese sus apellidos\n")
luga_naci=input("Ingrese lugar de Nacimiento\n")
localidad=input("Ingrese su localidad\n")
ubicacion=input("Ingrese su ubicacion\n")
edad=input("Ingrese su edad\n")
space=""
print("BIENVENIDO\n")
print("Su primer nombre es ",nombre,space,", su segundo nombre es ",segun_nombre,", sus apellidos son ",apellido+space,", nacio en la ciudad de ",luga_naci," actualmente usted vive en la ciudad de ",localidad," y su dirección actual es ",ubicacion," y tienes la edad de",space+edad," años")
edad=int(edad)
if edad >= 0 and edad <=11:
    print ("Es un niño, menor de edad.")
elif edad >= 12 and edad <=17:
    print ("Es un joven, menor de edad.")
elif edad >= 17 and edad <=35:
    print ("Es un joven, mayor de edad.")
elif edad >= 36 and edad <=65:
    print ("Es un adulto.")
else:
    print("Usted esta en la trcera edad.")
