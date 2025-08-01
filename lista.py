
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
    |    0. Sair                            |
    |                                       |
    |_______________________________________|""")

    
    tarefas = int(input("Qual tarefa você deseja adicionar?: "))
    
    if tarefas == 1:
        inserir = input("Insira a tarefa: ")
        lista.append(inserir)
    

    elif tarefas == 2:
        print(*lista) 

    elif tarefas == 3:
        escolher_item = input("Qual tarefa foi concluída?: ")
        for inserir in lista:
            if inserir == escolher_item:
                print(f"[X] {escolher_item}")


    elif tarefas == 0:
        print("Até mais!")
        break             





 
        

    