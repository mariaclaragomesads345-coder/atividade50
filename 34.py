"""Calcula a média somente das notas válidas entre dez entradas."""

QUANTIDADE_NOTAS = 10
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 10.0

print("=== Validação de notas ===")
print(f"Digite {QUANTIDADE_NOTAS} notas entre 0 e 10.")
print("Notas fora desse intervalo serão ignoradas.\n")

soma_notas_validas = 0.0
quantidade_notas_validas = 0

for aluno in range(1, QUANTIDADE_NOTAS + 1):
    while True:
        entrada = input(f"Digite a nota do aluno {aluno}: ").strip().replace(",", ".")
        try:
            nota = float(entrada)
            break
        except ValueError:
            print("Entrada inválida. Digite um número, como 7,5.\n")

    if nota < NOTA_MINIMA or nota > NOTA_MAXIMA:
        print(f"Nota {nota:g} inválida; será ignorada.\n")
        continue

    soma_notas_validas += nota
    quantidade_notas_validas += 1

print("\n=== Resultado ===")
print(f"Notas válidas: {quantidade_notas_validas} de {QUANTIDADE_NOTAS}")

if quantidade_notas_validas > 0:
    media = soma_notas_validas / quantidade_notas_validas
    print(f"Média das notas válidas: {media:.2f}")
else:
    print("Nenhuma nota válida foi informada; não é possível calcular a média.")
