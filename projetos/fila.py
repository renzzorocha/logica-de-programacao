def criarFila():
    return []

def inserirNaFila(fila, elemento):
    fila.append(elemento)

def removerDaFila(fila):
    fila.pop(0)

fila = criarFila()

inserirNaFila(fila, 5)
inserirNaFila(fila, 7)
inserirNaFila(fila, 8)
inserirNaFila(fila, 12)
inserirNaFila(fila, 15)
inserirNaFila(fila, 18)
inserirNaFila(fila, 33)
removerDaFila(fila)
print(fila)