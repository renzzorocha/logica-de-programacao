import os

comando = input('Olá, eu sou a sua assistete Pytrina. O que posso ajudar?: ')

match comando:
    case 'oi' | 'clean':
        print('Testandoooo!. Olá, programador.')
    case _:
        print('errooooor')