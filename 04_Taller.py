# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:32:59 2021

@author: David Suárez Molina
"""

while True:
    x=input('Ingrese el # que contaré: ')
    
    if x=='q' or x=='quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y+=1
        if y>x:
            break