
lista = []

while True:

    print("""     
     _______________________________________       
    |                                       |
    |               TO DO LIST              |
    |_______________________________________|
    |                                       |
    |    1. Inserir tarefa                  |
    |    2. Listar tarefas                  |
    |    3. Marcar como concluído           |
    |    4. Remover tarefa                  |
    |    0. SAIR                            |
    |                                       |
    |_______________________________________|""")

    
    tarefas = int(input("Qual tarefa você deseja adicionar?: "))
    
    if tarefas == 1:
        item = input("Insira a tarefa: ")
        lista.append(item)
    

    elif tarefas == 2:
        for item in lista:
            print(*item) 

    elif tarefas == 3:
        escolher_item = input("Qual tarefa foi concluída?: ")
        for item in lista:
            if item == escolher_item:
                print(f" {escolher_item}")

    elif tarefas == 4:
        for item in lista:
            print(item)
        escolher_item = input("Qual tarefa você quer excluir?: ")
        lista.remove(escolher_item)
                

    elif tarefas == 0:
        print("Até mais!")
        break             





 
        

    