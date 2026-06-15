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
    print(f"Nome: {funcionario['nome']} ")
    print(f"Idade: {funcionario['idade']} ")
    print(f"Cargo: {funcionario['cargo']} ")
    print()

none = input("Digite o nome do funcionario para buscar: ")

if none == {none}:
    print(f"funcionario {none} encontrado")
else:
    print(f"funcionario {none} não encontrado")