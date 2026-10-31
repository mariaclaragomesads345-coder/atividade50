print("--- TABUADA DE MULTIPLICAÇAO ---")

#tratamento de entrada para garantir que o usuario digite um numero interio valido
while True:
    try:
        numero = int(input("Digite um numero inteiro para ver a tabuada: "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

print(f"\nTabuada do {numero}:")

#variavel de controle para o multiplicador (começa em 1)
multiplicador = 1

# Executa o loop ate 10
while multiplicador <= 10:
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
    multiplicador += 1 # incrementa o multiplicador a cada ciclo