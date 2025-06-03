def adicionar_tarefa(lista_de_tarefas, tarefa):
    # Adiciona uma tarefa à uma lista
    lista_de_tarefas.append(tarefa)
    print("Tarefa adicionada!")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    # Exibe lista de tarefas numeradas
    print("\n*" * 50)
    print(f"{' ' * 15}Lista de Tarefas")
    print("-" * 50)
    n = 1
    for tarefa in lista_de_tarefas:   
        print(f"{n} - {tarefa}")
        n += 1 
    print("*" * 50)

def deletar_tarefa(lista_de_tarefas, tarefa):
    # Deleta tarefa de uma lista pré-existente através do número
    lista_de_tarefas.pop((tarefa - 1))
    print("Tarefa deletada!")
    return lista_de_tarefas

def exibir_menu():
    # Exibe menu de opções 
    print('Escolha uma opção:\n' \
      '1 - Inserir nova tarefa\n' \
      '2 - Listar tarefas\n' \
      '3 - Deletar tarefa\n' \
        '4 - Sair')


lista_de_tarefas = list()
continuar = True 
print("\n")
print("*" * 50)
print("Olá, essa é sua lista de tarefas!")
print("*" * 50)

while continuar:
    exibir_menu()
    opcao = input('Insira o que deseja fazer: ')

    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)

    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)

    elif opcao == "3":
        # A validação verifica se o valor inserido é numérico 
        tarefa = input("Insira o número da tarefa que deseja deletar: ")
        if not tarefa.isnumeric():
            print("Número inválido")  
            tarefa = int(tarefa)
        elif int(tarefa) > len(lista_de_tarefas):
            print("Número inválido")     
        elif int(tarefa) <= 0:
            print("Número inválido")
        else:
            deletar_tarefa(lista_de_tarefas, int(tarefa)) 
    elif opcao == "4":
        continuar = False

    else:
     print("Opção inválida")
    print('\n')

