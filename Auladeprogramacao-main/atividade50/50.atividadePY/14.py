#lista para armazenar os nomes dos alunos cadastrados
alunos = []

while True:
    #Solicite o nome do aluno
    nome = input("Digite o nome do aluno: ").strip()
    alunos.append(nome)

    #pergunta se deseja continuar
    continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
    if continuar != 's':
        break

    #se a resposta não for 's', ou 'sim', o loop é encerrado
    if continuar not in ['s', 'sim']:
        break

# Exibe o resultado final com todos os alunos cadastrados
print("\nAlunos cadastrados:")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")