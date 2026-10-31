"""Busca um número inteiro e apresenta o índice em que foi encontrado."""

numeros = [14, 27, 5, 32, 18, 9, 41, 23, 6, 35]

print("=== Busca de número por índice ===")
print(f"Lista: {numeros}")
print("Os índices começam em 0.\n")

while True:
    try:
        valor_buscado = int(input("Digite um número inteiro para buscar: ").strip())
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.\n")

indice_encontrado = -1
for indice, numero in enumerate(numeros):
    if numero == valor_buscado:
        indice_encontrado = indice
        break

if indice_encontrado != -1:
    print(f"O número {valor_buscado} foi encontrado no índice {indice_encontrado}.")
else:
    print(f"O número {valor_buscado} não existe na lista.")
