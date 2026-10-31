def exibir_menu():
    print("\n--- MENU INTERATIVO ---")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")


def obter_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2


def executar_menu():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4) ou 'sair' para encerrar: ")

        if opcao == "sair":
            print("\nSaindo do programa. Até logo!")
            break
        elif opcao == "1":
            n1, n2 = obter_numeros()
            print(f"\nResultado da soma: {n1} + {n2} = {n1 + n2}")
        elif opcao == "2":
            n1, n2 = obter_numeros()
            print(f"\nResultado da subtração: {n1} - {n2} = {n1 - n2}")
        elif opcao == "3":
            n1, n2 = obter_numeros()
            print(f"\nResultado da multiplicação: {n1} * {n2} = {n1 * n2}")
        elif opcao == "4":
            n1, n2 = obter_numeros()
            if n2 == 0:
                print("\nNão é possível dividir por zero.")
            else:
                print(f"\nResultado da divisão: {n1} / {n2} = {n1 / n2}")
        else:
            print("\nOpção inválida! Por favor, escolha um número de 1 a 4.")


if __name__ == "__main__":
    executar_menu()
                   



