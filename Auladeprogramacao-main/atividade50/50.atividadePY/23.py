#inicializa a variavel acumuladora para armazenar a soma dos pares
soma_pares = 0

print("=== Soma dos numeros pares (1 a 100) ===")
print(" Processando o calculo...")

for numero in range(2, 101, 2):
    soma_pares += numero #acumula valor do numero par atual

print(f"\nA soma dos números pares de 1 a 100 é: {soma_pares}")