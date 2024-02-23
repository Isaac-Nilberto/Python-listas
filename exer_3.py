#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:37:59 2024

@author: isaacnilberto
"""
'''
Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os
em uma lista, ja na posicao correta de insercao. No final, mostre a lista ordenada
na tela.
'''
lista = []

for i in range(0,5):
    numero = int(input('Digite um valor a ser adicionado a lista: '))
    if i == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                
                lista.append(pos, numero)
                break
            pos += 1
            
        
print(f'A lista ordenada é: {lista}')
            
        
