"""Encontra o maior valor e seu índice percorrendo uma lista de 20 números."""

numeros = [18, 42, 7, 95, 31, 64, 12, 83, 56, 29,
           71, 4, 88, 37, 20, 99, 53, 10, 76, 45]

print("=== Maior valor e seu índice ===")
print(f"Lista: {numeros}\n")

maior_valor = numeros[0]
indice_maior = 0

for indice in range(1, len(numeros)):
    if numeros[indice] > maior_valor:
        maior_valor = numeros[indice]
        indice_maior = indice

print(f"Maior valor: {maior_valor}")
print(f"Índice do maior valor: {indice_maior}")
