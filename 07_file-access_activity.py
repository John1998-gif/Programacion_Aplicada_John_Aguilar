# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:38:26 2021

@author: Acer
"""

file=open('devices.txt',"a")
while True:
    newItem=input("Ingrese un nuevo Item:")
    if newItem == "exit":
        print("ALL DONE!!")
        break
    else:
        file.write(newItem + "\n")
file.close()