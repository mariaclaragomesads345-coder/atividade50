#solicita o primeiro valor ao usuario
numero = int(input("Digite um numero inteiro positivo: "))

#enquanto o numero for menor ou igual a 0, continua solicitando
while numero <= 0:
    print("o numero digitado nao é positivo, tente novamente")
    numero = int(input("Digite um numero inteiro positivo: "))

print(f"sucesso! o numero foi digitado corretamente: {numero}")