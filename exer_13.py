#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:52:51 2024

@author: isaacnilberto
"""

'''
Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em
uma lista composta. No final, mostre um boletim contendo a media de cada um e 
permita que o usuario possa mostrar as notas de cada aluno individualmente.
'''

lista_completa = []
lista = []
notas = 0
while True:
    nome = str(input('Qual o nome do aluno: ').upper())
    lista.append(nome)
    for nota in range(0,2):
        notas = float(input(f'Qual o valor da nota{nota + 1}? '))
        lista.append(notas)
    lista_completa.append(lista[:])
    lista.clear()
    continuador = str(input('Voce deseja continuar? [S/N] '))
    while continuador not in 'SsNn':
        continuador = str(input('Voce digitou um comando errado, para continuar digite S ou N: '))
    if continuador in 'Nn':
        break

for linha in lista_completa:
    print(f'A media do aluno {linha[0]} é {(linha[1] + linha[2])/2}')

print(f'======== Boletim ========')

for linha in lista_completa:
    print(f'Aluno {linha[0]}:')
    print(f'nota 1: {linha[1]}  nota 2: {linha[2]}')
        