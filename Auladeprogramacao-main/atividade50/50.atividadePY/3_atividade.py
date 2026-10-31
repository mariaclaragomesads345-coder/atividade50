soma = 0

print("--- SOMA DE NUMEROS---")
print("Digite numeros interios (digite 0 para encerrar e ver o resultado):")

while True:
    try:
        numero = int(input("Digite um numero: "))

        #condiçao de parada: se o numero for 0, sai do loop
        if numero == 0:
            break   

        #acumula o valor na soma total
        soma += numero

    except ValueError:
        print("Erro: digite apenas numeros inteiros validos. tente novamente.")

    print(f"\nA soma de todos os numeros informados é: {soma}")