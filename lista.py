
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
            print(item) 

    elif tarefas == 3:
        indice = 0
        for item in lista:
            print(f"{indice} {item}")
            indice += 1
        c = int(input("Qual o índice da tarefa foi concluída?: "))
        lista[c] ="(✗)" + lista[c]
        print("Concluído!")

    elif tarefas == 4:
        for item in lista:
            print(item)
        c = input("Qual tarefa você quer excluir?: ")
        lista.remove(c)
        for item in lista:
            print(item)
        
            
    elif tarefas == 0:
        print("Até mais!")
        break             





 
        

    