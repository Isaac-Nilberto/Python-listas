#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:37:50 2024

@author: isaacnilberto
"""
'''
Crie um programa onde o usuario possa digitar varios valores numericos e cadas-
tre-os em uma lista. Caso o numero ja exista la dentro, ele nao sera adicionado.
No final, serao exibidos todos os valores unicos digitados, em ordem crescente.
'''

valores = []
print('='*30)

valor = 0
while True:
    valor = int(input('Digite um numero a ser adicionado a lista: '))
    if valor not in valores:
        valores.append(valor)
    else:
        print('Esse valor ja esta na lista e nao sera adicionado!.')
        
    #while valores not in valores:
    #    valores.append(int(input('Esse valor ja esta na lista, digite um novo valor: ')))
        
    print('='*30)
    continuador = str(input('Voce deseja continuar [S/N]? '))
    print('='*30)
    
    
    
    while continuador not in 'SsNn':
        continuador = str(input('Voce digitou um comando desconhecido para continuar [S/N]? '))
        print('='*30)
    
    if continuador in 'Nn':
        break
    
    if continuador in 'Ss':
        continue
    
print(f'A lista contem os seguintes valores: {valores}')

print(f'Em ordem crescente: {sorted(valores)}')
    
#%%%

valores