# Armazenar funcionarios, (lista de funcionarios)
funcionarios = [
    {
        "id": 1,
        "nome": "Kayque",
        "idade": 16,
        "cargo": "jovem aprendiz/repositor"
    },
    {
        "id": 2,
        "nome": "Debora",
        "idade": 28,
        "cargo": "Adiministradora"
    },
    {
        "id": 3,
        "nome": "Paula",
        "idade": 30,
        "cargo": "Gerente"
    },
    {
        "id": 4,
        "nome": "Ana",
        "idade": 24,
        "cargo": "Caixa"
    },
    {
        "id": 5,
        "nome": "Fabiano",
        "idade": 45,
        "cargo": "Estorquista"
    }
]
# Imprimir os funcionarios. dicionario.
for funcionario in funcionarios:
    print(f"ID: {funcionario['id']} ")
    print(f"Nome: {funcionario['nome']} ")
    print(f"Idade: {funcionario['idade']} ")
    print(f"Cargo: {funcionario['cargo']} ")
    print()
#buscar um funcionario pelo nome
nome_buscado = input("Digite o nome do funcionario para buscar: ")



for funcionario in funcionarios:
    if nome_buscado == funcionario['nome']:
        print(f"Funcionario encontrado")
        print(f"ID: {funcionario['id']}")
        print(f"Nome: {funcionario['nome']}")
        print(f"Idade: {funcionario['idade']}")
        print(f"Cargo: {funcionario['cargo']}")
        break
else:
        print("Funcionario não encontrado")


#adicionar um novo funcionario
novo_nome = input("Digite o nome do novo funcionario: ")
nova_idade = int(input("Digite a idade do novo funcionario: "))
novo_cargo = input("Digite o cargo do novo funcionario: ")

novo_funcionario = {
    "id": len(funcionarios) + 1,
    "nome": novo_nome,
    "idade": nova_idade,
    "cargo": novo_cargo
}


print()

funcionarios.append(novo_funcionario)
print("Novo funcionario adicionado com sucesso!")


print()


for funcionario in funcionarios:
    print(f"ID: {funcionario['id']} ")
    print(f"Nome: {funcionario['nome']} ")
    print(f"Idade: {funcionario['idade']} ")
    print(f"Cargo: {funcionario['cargo']} ")
    print()

nome_atualizar = input("digite o nome do funcionario para atualizar: ")

for funcionario in funcionarios:
     if nome_atualizar == funcionario['nome']:
        novo_cargo = input("Digite o novo cargo do funcionario: ")
        funcionario['cargo'] = novo_cargo
        print()
        print("Cargo atualizado com sucesso!")
        break
else:
     print("Funcionario não encontrado")

print()

remover_funcionario = input ("Digite o nome do funcionario para remover: ")

for funcionario in funcionarios:
     if remover_funcionario == funcionario['nome']:
        print("Funcionario encontrado")
        funcionarios.remove(funcionario)
        print()
        print("Removendo funcionario...")
        print()
        print("Funcionario removido com sucesso!")
        break
else:
        print("Funcionario não encontrado")

print()


for funcionario in funcionarios:
    print(f"ID: {funcionario['id']} ")
    print(f"Nome: {funcionario['nome']} ")
    print(f"Idade: {funcionario['idade']} ")
    print(f"Cargo: {funcionario['cargo']} ")
    print()