soma = 0
quantidade = 0

print("--- CALCULO DE MEDIA DE NOTAS ---")
print("Digite as notas dos alunos (digite -1 para encerrar e ver a media):")

while True:
    try:
        nota = float(input("Digite a nota do aluno: "))

        # Condição de parada: se a nota for -1, sai do loop.
        if nota == -1:
            break

        # Validação para garantir que a nota está no intervalo padrão (0 a 10).
        if 0 <= nota <= 10:
            soma += nota
            quantidade += 1
        else:
            print("Erro: digite uma nota entre 0 e 10.")
    except ValueError:
        print("Erro: digite um número válido.")

# Verifica se foram inseridas notas para evitar divisão por zero.
if quantidade > 0:
    media = soma / quantidade
    print(f"\nA média das notas informadas é: {media:.2f}")
else:
    print("\nNenhuma nota foi informada.")