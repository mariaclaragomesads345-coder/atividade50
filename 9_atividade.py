print("--- CALCULO DE FATORIAL ---")

while True:
    try:
        numero = int(input("Digite um numero inteiro nao negativo: "))
        if numero < 0:
            print("Erro: digite um numero inteiro nao negativo. \n")
            continue
        break
    except ValueError:
        print("Erro: digite um numero inteiro valido. \n")

fatorial = 1
contador = numero

while contador > 1:
    fatorial *= contador
    contador -= 1

print(f"\nO fatorial de {numero} é: {fatorial}")
           
        