from collections import deque

def criarFila():
    return deque()

def inserirNaFila(fila, elemento):
    fila.append(elemento)

def removerDaFila(fila):
    fila.popleft()

fila = criarFila()

inserirNaFila(fila, 4)
inserirNaFila(fila, 5)
inserirNaFila(fila, 6)
inserirNaFila(fila, 7)
inserirNaFila(fila, 8)
inserirNaFila(fila, 9)
inserirNaFila(fila, 0)
removerDaFila(fila)
removerDaFila(fila)
removerDaFila(fila)
print(fila)
