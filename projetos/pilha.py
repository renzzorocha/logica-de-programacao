def criarPilha():
    return []

def inserirNaPilha(pilha, elemento):
    pilha.append(elemento)

def removerDaPilha(pilha):
    pilha.pop()

pilha = criarPilha()

inserirNaPilha(pilha, 4)
inserirNaPilha(pilha, 5)
inserirNaPilha(pilha, 6)
inserirNaPilha(pilha, 7)
inserirNaPilha(pilha, 8)
inserirNaPilha(pilha, 9)
inserirNaPilha(pilha, 0)
removerDaPilha(pilha)
removerDaPilha(pilha)
removerDaPilha(pilha)
print(pilha)