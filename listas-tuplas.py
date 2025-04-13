tarefas = []

def adicionarTarefas(tarefa):
    novaTarefa = (tarefa, "pendente")
    tarefas.append(novaTarefa)

def exibirTarefas():
    for tarefa in tarefas:
        print(f'{tarefa[0]} - Status: {tarefa[1]}')

def concluirTarefa(tarefa):
    for t in tarefas:
        if t[0] == tarefa:
            t[1] = 'concluída'
            break


adicionarTarefas('Comer bosta')
exibirTarefas()
print('Agora vou concluir a tarefa')
concluirTarefa('Comer bosta')
exibirTarefas()
