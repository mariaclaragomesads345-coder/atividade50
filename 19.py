notas = []

print("Por favor! informe 5 notas dos alunos:")
for i in range(1, 6):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"A média das 5 notas digitadas é: {media:.2f}")

if media >= 7.0:
    print("Parabéns! O aluno foi aprovado.")
else:
    print("O aluno não foi aprovado. Estude mais para a próxima vez!")