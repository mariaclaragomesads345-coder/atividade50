print("=== Calculadora de Potenciação ===")

base = float(input("Digite o valor da base: "))

while True:
    expoente = int(input("Digite o valor do expoente (deve ser um número inteiro): "))
    if expoente >= 0:
        break
    print("O expoente deve ser um número inteiro não negativo. Tente novamente.")

resultado = 1

for _ in range(expoente):
    resultado *= base

print(f"O resultado de {base} elevado a {expoente} é: {resultado}")