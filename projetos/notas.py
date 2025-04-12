nota = int(input('Informe a nota do aluno: '))

if nota > 18:
    print('Passou de Ano! Congrats')
elif nota < 18:
    print('Bombou de Ano! Se ferrou')
else:
    print('Erro ao ler a nota. Favor inserir um número válido.')
