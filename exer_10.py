#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:37:20 2024

@author: isaacnilberto
"""

'''
Crie uma matriz de dimensao 3 x 3 e preencha os valores lidos pelo teclado.
No final, mostre a matriz na tela com a formatacao correta.
'''

matrix = [[],[],[]]
for linha in range(len(matrix[0:3])):
    #numero = int(input('Valor a ser adicionado: '))
    for coluna in range(0,3):
        numero = int(input(f'Valor a ser adicionado na linha {linha} x coluna {coluna}: '))
        matrix[linha].append(numero)

for linha in range(3):
    for coluna in range(3):
        print(matrix[linha][coluna], end = ' ')
    print()