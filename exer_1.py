#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:37:40 2024

@author: isaacnilberto
"""

'''
Faca um programa que leia 5 valores e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respecti-
vas posicoes na lista.
'''
valores = []

for i in range(0,5):
    valor = int(input('Digite um valor:'))
    valores.append(valor)
    

minimo = min(valores)
maximo = max(valores)

for indice, valor in enumerate(valores):
    if valor == maximo:    
        print(f'O indice-{indice}- nos mostra o valor maximo: {maximo}')
    if valor == minimo:    
        print(f'O indice-{indice}- nos mostra o valor maximo: {minimo}')
    
