import os

print('Bem-vindo ao DETRAN!')
print('Este é o novo teste extremamente complexo para liberar ou não a CNH')
print()
idade = int(input('Digite a sua idade: '))
if idade >= 18:
    os.system('clear')
    print('Pode dirigir!')
else:
    os.system('clear')
    print('Não pode dirigir')


    