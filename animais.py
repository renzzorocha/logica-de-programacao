perguntas = [['O seu animal gosta de banana?', 'Macaco']]

while True:
    print('Pense em um animal...')
    
    acertou = False
    
    for pergunta in perguntas:
     resposta = input(f'{pergunta[0]} (s/n): ')
    if resposta.lower() == 's':
        print(f'O animal que você pensou é o: {pergunta[1]}')
        acertou = True
        
    if not acertou:
        animal = input('Droga! Não consegui adivinhar qual animal você pensou... Qual animal seria?: ')
        nova_pergunta = input('Qual pergunta você faria para encontra-lo?: ')
        perguntas.append([nova_pergunta, animal])
    
    resposta = input('Gostaria de jogar novamente? (s/n): ')
    if resposta.lower() != 's':
           print('Foi um prazer jogar com você, jovem!')
           break