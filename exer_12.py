#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:37:35 2024

@author: isaacnilberto
"""

'''
Faca um programa que ajude um jogador da mega sena a criar palpites. O programa
vai perguntar quantos jogos serao gerados e vai sortear seis numeros entre 1 e 60 para
cada jogo, cadastrando tudo em uma lista composta.
'''
import random

numero_jogos = int(input('Quantos jogos desejas gerar? '))
lista_jogos = []
jogos = []

for numero_jogo in range(numero_jogos):
    print(f'Jogo de numero {numero_jogo + 1}')
    for jogo in range(0,6):
        jogos.append(random.randint(0,60))
    
    lista_jogos.append(jogos[:])
    print(f'{jogos}')
    print('='*30)

    jogos.clear()
print('='*30)
for numero, lista_jogo in enumerate(lista_jogos):
    print(f'O jogo de numero {numero + 1} é {lista_jogo}')