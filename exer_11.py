#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:37:27 2024

@author: isaacnilberto
"""

'''
Aprimore o desafio anterior, mostrando no final:
    a) A soma de todos os valores pares digitados;
    b) A soma dos valores da terceira coluna;
    c) O maior valor da segunda linha.
'''

matrix = [[],[],[]]
soma = 0
for linha in range(len(matrix[0:3])):
    #numero = int(input('Valor a ser adicionado: '))
    for coluna in range(0,3):
        numero = int(input(f'Valor a ser adicionado na linha {linha} x coluna {coluna}: '))
        soma += numero
        matrix[linha].append(numero)
print('-='*30)
print('A matrix é \n')

for linha in range(3):
    for coluna in range(3):
        print(matrix[linha][coluna], end = ' ')
    print()
    
print('-='*30)

soma_par = 0


for linha in range(len(matrix)):
    for coluna in range(len(matrix[linha])):
        if matrix[linha][coluna] % 2 == 0:
            soma_par += matrix[linha][coluna]

soma_coluna = 0
for linha in range(len(matrix)):
    for coluna in range(2,len(matrix[linha])):
        soma_coluna += matrix[linha][coluna]
print('-='*30)
print(f'A soma de todos os valores é {soma}.')
print('-='*30)
        
print(f'A soma dos valores pares é {soma_par}.')

print('-='*30)

print(f'O maior valor da segunda linha é {max(matrix[1])}.')