"""Cadastra dez alunos e verifica se um nome está na lista."""

QUANTIDADE_ALUNOS = 10
nomes_alunos = []

print("=== Cadastro de alunos ===")
for numero_aluno in range(1, QUANTIDADE_ALUNOS + 1):
    while True:
        nome = input(f"Digite o nome do {numero_aluno}º aluno: ").strip()
        if nome:
            nomes_alunos.append(nome)
            break
        print("O nome não pode ficar vazio. Tente novamente.")

print("\n=== Busca de aluno ===")
while True:
    nome_buscado = input("Digite o nome que deseja procurar: ").strip()
    if nome_buscado:
        break
    print("O nome não pode ficar vazio. Tente novamente.")

nomes_normalizados = [nome.casefold() for nome in nomes_alunos]
if nome_buscado.casefold() in nomes_normalizados:
    print(f"{nome_buscado} está cadastrado(a).")
else:
    print(f"{nome_buscado} não está cadastrado(a).")
