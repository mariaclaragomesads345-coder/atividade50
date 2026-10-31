print("--- MAIOR NUMERO ---")
print("Digite numeros inteiros (digite 0 para encerrar):")

maior = None

while True:
  try:
    numero = int(input("Digite um numero: "))

    if numero == 0:
      break

    if maior is None or numero > maior:
        maior = numero

  except ValueError:
    print("Erro: digite apenas numeros inteiros validos. tente novamente.")

if maior is not None:
    print(f"\nO maior numero informado é: {maior}")
else:
    print("\nNenhum numero valido foi informado.")
