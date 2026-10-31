print("=== Soma de Numeros Não Negativos (10 Entradas) ===")
print("Por favor, informe 10 numeros inteiros.\n")

soma_nao_negativos = 0

for i in range(1, 11):
    while True:
        try:
            numero = int(input(f"Digite o {i}° numero inteiro: "))
            break
        except ValueError:
            print(" Entrada invalida! digite apenas numeros inteiros.\n")

    if numero < 0:
        print(f" Numero {numero} é negativo. ignorando pelo comando continue.\n")
        continue

    soma_nao_negativos += numero

print("\n" + "=" * 55)
print(f" A Soma total dos numeros nao negativos é: {soma_nao_negativos}")
print("=" * 55)