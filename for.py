# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:24:52 2021

@author: John Aguilar
"""

lista1=['R1','R2','R3',"S1","S2","S3"]
switches=[]
routers=[]

for i in lista1:
    if "R" in i:
        routers.append(i)
    if "S" in i:
        switches.append(i)

for i in routers:
    print(i)
    
for i in switches:
    print(i)