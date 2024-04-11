
"""
    lista = []
    lista.append("v1")
    lista.append("v2")
    lista.append("v3")
    print(lista)
"""




"""
frutas = []
frutas.append("maça")
frutas.append("bergamota")
frutas.append("banana")
frutas.append("melão")
frutas.append("laranja")


print(frutas)
print(len(frutas))
frutas.pop(0)
print(frutas)
frutas.pop(-1)
print(frutas)
print(len(frutas))
print(frutas[0])
print(len(frutas[0]))
frutas.clear()
print(frutas)
# print(f"frutas selecionadas: {frutas[0]} e {frutas[2]}")
"""

"""
tarefas = []

for i in range(0,10):
    tarefa = input(f"digite a tarefas número {i + 1}: ")
    tarefas.append(tarefa)
print(tarefas)
"""

tarefas = []
contador = 0
while contador < 10:
    tarefa = input(f"digite a tarefa número {contador + 1}: ")
    tarefas.append(tarefa)
    contador += 1
print(tarefas)