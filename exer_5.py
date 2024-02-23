#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:38:14 2024

@author: isaacnilberto
"""

'''
Crie um programa que vai ler varios numeros e colocar em uma lista.

Depois disso, crie duas listas extras que vao conter apenas os valores pares e
os impares digitados, respectivamente.

Ao final, mostre o conteudo das tres listas geradas.
'''
valores = []
print('='*40)
while True:
    valor = int(input('Digite um valor para adicionar a lista: '))
    
    valores.append(valor)
    
    continuador = str(input('Desejas continuar? [S/N] '))
    print('='*40)
    while continuador not in 'SsNn':
        continuador = str(input('Voce digitou um comando inválido. Desejas continuar? [S/N] '))
        print('='*40)
    if continuador in 'Nn':
        break
    if continuador in 'Ss':
        continue

par = []
impar = []

for valor in range(len(valores)):
    if valores[valor] % 2 == 0:
        par.append(valores[valor])
    else:
        impar.append(valores[valor])


print(f'A lista original é {valores}.')
print('='*30)
print(f'A lista com numeros pares é {par}.')
print('='*30)
print(f'A lista com numeros impares é {impar}.')
    