#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:36:52 2024

@author: isaacnilberto
"""

'''
Faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma
lista, no final:
    a) quantas pessoas foram cadastradas;
    b) Uma listagem com as pessoas mais pesadas;
    c) Uma listagem com as pessoas mais leves.
'''

lista_completa = []
dados = []
peso_min = 0
peso_max = 0

while True:
    dados.append(str(input('Nome: ')).upper())
    dados.append(int(input('Peso: ')))
    lista_completa.append(dados[:])
    dados.clear()
    
    continuador = str(input('Queres continuar? [S/N] '))
    while continuador not in 'SsNn':
        continuador = str(input('Voce digitou um comando errado. Queres continuar? [S/N] '))
    if continuador in 'Nn':
        break
    if continuador in 'Ss':
        continue
