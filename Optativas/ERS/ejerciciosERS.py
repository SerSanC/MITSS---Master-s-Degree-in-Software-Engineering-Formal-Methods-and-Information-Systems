#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:21:40 2020

@author: sergisanz
"""


# Ejercicio 1
def max ():
    x = int(input("Valor 1: "))
    y = int(input("Valor 2: "))
    if x>y:
        return print(x)
    else:
        return print(y)
# Ejercicio 2
def isVocal():
    n = input("Introduzca una letra: ")
    if len(n) == 1:

        if n == n.lower():
            if n in ("a","e","i","o","u"):
                print ("es minuscula y vocal")
            else:
                print ("es minuscula y consonante")
 
        else:
            if n in ("A","E","I","O","U"):
                print ("es mayuscula y vocal")
            else:
                print ("es mayuscula y consonante")
    else:
        print("Tamaño incorrecto")
        
# Ejercicio 3
def sum ():
    a = [int(x) for x in input().split()]
    print(a)
# Ejercicio 4
def reverse():
    rev = input("Introducir text:")
    var = " "
    for i in reversed(rev):
        var = var + i
    print ((var))
# Ejercicio 5
def pangrama():
    abecedario="abcdefghijklmnñopqrstuvwxyz"

    cadena= input("Introducir cadena:")
    faltan=False
    
    for i in abecedario:
        if not i in cadena:
            faltan=True
            break
     
    if faltan==False:
        print("Estan todas las letras")
    else:
        print("no estan todas las letras")
# Ejercicio 6
def char_freq():
    
if __name__ == '__main__':
    #max()
    #sum()
    #isVocal()
    #reverse()
    #pangrama()
    
    
    
    
    