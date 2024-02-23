#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:38:20 2024

@author: isaacnilberto
"""
'''
Crie um programa onde o usuario digite uma expressao qualquer que use parenteses.
Seu aplicativo devera analisar se a expressao passada esta com os parenteses abertos
e fechados na ordem correta.
'''

expressao = str((input('Digite a expressao: ')))

pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta valida')
else:
    print('Sua espressao nao esta valida.')
        