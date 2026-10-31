"""Realiza uma busca linear em uma lista de dez números inteiros."""

numeros = [12, 7, 25, 3, 18, 40, 9, 31, 5, 22]

print("=== Busca linear ===")
print(f"Lista: {numeros}")

while True:
    try:
        numero_buscado = int(input("Digite um número inteiro para buscar: ").strip())
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.\n")

presente = False

for numero in numeros:
    if numero == numero_buscado:
        presente = True
        break

if presente:
    print(f"O número {numero_buscado} está presente na lista.")
else:
    print(f"O número {numero_buscado} não está presente na lista.")
