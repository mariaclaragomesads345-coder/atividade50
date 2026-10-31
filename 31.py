print("=== Numeros Impares entre 1 e 100 ===")

# percorre todos os numeros de 1 a 100
for numero in range(1, 101):
    if numero % 2 == 0:
        continue
    print(numero)

print("\nFim da Contagem!")