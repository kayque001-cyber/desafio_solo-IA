import json

def carregar_funcionarios():
    with open("funcionarios.json", "r") as arquivo:
        funcionarios = json.load(arquivo)
    return funcionarios

def salvar_funcionarios():
    with open("funcionarios.json", "w") as arquivo:
        json.dump(funcionarios, arquivo, indent=4)



# Armazenar funcionarios, (lista de funcionarios)
funcionarios = carregar_funcionarios()


def encontrar_funcionario(nome):
    for funcionario in funcionarios:
        if nome.lower() == funcionario["nome"].lower():
            return funcionario
    return None




# Imprimir os funcionarios. dicionario.
def listar_funcionarios():
    for funcionario in funcionarios:
        print(f"ID: {funcionario['id']} ")
        print(f"Nome: {funcionario['nome']} ")
        print(f"Idade: {funcionario['idade']} ")
        print(f"Cargo: {funcionario['cargo']} ")
        print()



#buscar um funcionario pelo nome
def buscar_funcionario():
    nome_buscado = input("Digite o nome do funcionario para buscar: ")

    funcionario = encontrar_funcionario(nome_buscado)
    if funcionario:
            print(f"Funcionario encontrado")
            print(f"ID: {funcionario['id']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Idade: {funcionario['idade']}")
            print(f"Cargo: {funcionario['cargo']}")

    else:
            print("Funcionario não encontrado")



#adicionar um novo funcionario
def adicionar_funcionario():
    novo_nome = input("Digite o nome do novo funcionario: ")
    nova_idade = int(input("Digite a idade do novo funcionario: "))
    novo_cargo = input("Digite o cargo do novo funcionario: ")
    
    novo_id = max(funcionario["id"] for funcionario in funcionarios) + 1
    
    novo_funcionario = {
        "id": novo_id,
        "nome": novo_nome,
        "idade": nova_idade,
        "cargo": novo_cargo
    }


    print()

    funcionarios.append(novo_funcionario)
    salvar_funcionarios()
    print("Novo funcionario adicionado com sucesso!")


    print()
def atualizar_funcionario():
    nome_atualizar = input("digite o nome do funcionario para atualizar: ")

    funcionario = encontrar_funcionario(nome_atualizar)
    if funcionario:
        novo_cargo = input("Digite o novo cargo do funcionario: ")
        funcionario['cargo'] = novo_cargo

        salvar_funcionarios()

        print()
        print("Cargo atualizado com sucesso!")

    else:
        print("Funcionario não encontrado")

def remover_funcionario():
    nome_remover = input ("Digite o nome do funcionario para remover: ")

    funcionario = encontrar_funcionario(nome_remover)
    if funcionario:
            print("Funcionario encontrado")
            funcionarios.remove(funcionario)

            salvar_funcionarios()
            
            print()
            print("Funcionario removido com sucesso!")

    else:
            print("Funcionario não encontrado")



def mostrar_menu():
    print("===== SISTEMA ATAC WEST =====")
    print("1 - Listar funcionários")
    print("2 - Buscar funcionário")
    print("3 - Adicionar funcionário")
    print("4 - Atualizar funcionário")
    print("5 - Remover funcionário")
    print("6 - Sair")
    print()

    opcao = input("Escolha uma opção: ").strip()

    print()

    if opcao == "1":
        listar_funcionarios()
    elif opcao == "2":
        buscar_funcionario()
    elif opcao == "3":
        adicionar_funcionario()
    elif opcao == "4":
        atualizar_funcionario()
    elif opcao == "5":
        remover_funcionario()
    elif opcao == "6":
        print("Encerrano sistema...")
    else:
        print("Opção inválida")

    return opcao

while True:
    opcao = mostrar_menu()

    if opcao == "6":
        print("Sistema finalizado.")
        break
