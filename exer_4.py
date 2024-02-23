#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:38:06 2024

@author: isaacnilberto
"""
'''
Crie um programa que lera varios numeros e colocar em uma lista. Depois mostre:
    a) Quantos numeros foram digitados;
    b) a lista de valores ordenada de forma decrescente;
    c) se o valor 5 foi digitado e esta ou nao na lista.
'''
valores = []

while True:
    
    valor = int(input('Digite um valor a ser adicionado a lista: '))
    valores.append(valor)
    
    continuador = str(input('Voce deseja continuar: [S/N]? '))
    while continuador not in 'SsNn':
        continuador = str(input('Voce digitou um comando desconhecido. Para continuar: [S/N]? '))
    
    if continuador in 'Nn':
        break
    
    if continuador in 'Sn':
        continue
    
    
    
print(f'Foram adicionados {len(valores)}')
print(f'='*30)
print(f'Os valores em ordem decrescene {sorted(valores, reverse = True)}.')
print(f'='*30)
if 5 in valores:
    print(f'O numero 5 esta na lista e esta na posicao {valores.index(5)}.')
else:
    print('O numero 5 nao esta na lista.')
