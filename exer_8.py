#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:37:02 2024

@author: isaacnilberto
"""

'''
Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os
em uma lista unica que mantenha separados os valores pares e impares. No final
mostre os valores pares e impares em ordem crescente.
'''
lista_completa = []
pares = []
impares = []
for i in range(0,7):
    numero = int(input(f'Digite o {i+1} valor que será analisado: '))
    if numero % 2 == 0:
        print('O numero é par.')
        pares.append(numero)
        
    else:
        print('O Numero é impar.')
        impares.append(numero)
        
lista_completa.append(pares[:])    
lista_completa.append(impares[:])
print('-='*30)
print(f'Lista completa {lista_completa}')

print('-='*30)
print(f'Os numeros pares em ordem crescente sao {sorted(lista_completa[0])}.')

print('-='*30)
print(f'Os numeros impares em ordem crescente sao {sorted(lista_completa[1])}.')