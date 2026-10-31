soma = 0 

print(" Por favor! informe 10 numeros interios:")
for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))
    soma += numero

print(f"A soma dos 10 números digitados é: {soma}")