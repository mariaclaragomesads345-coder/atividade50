"""Exibe os números de 1 a 100 que não são múltiplos de três."""

print("=== Números de 1 a 100, exceto múltiplos de 3 ===")

for numero in range(1, 101):
    if numero % 3 == 0:
        continue

    print(numero)

print("Fim da listagem.")
