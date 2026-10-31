print("=== Sistemas de controle de estoque ===")

while True:
    try:
        estoque = int(input("Digite a quantidade inicial de produtos no estoque:"))
        if estoque > 0:
            break
        print("o estoque inicial deve ser um numero inteiro maior que zero.\n")
    except ValueError:
        print("Digite um número inteiro válido.")

while estoque > 0:
    print(f"\n estoque atual disponivel: {estoque} unidade(s)")

    try:
        retirada = int( input("Digite a quantidade que deseja retirar: "))

        if retirada <= 0:
            print(" A quantidade de retiradas deve ser maior que zero, ou tente novamente> ")
            continue

        if retirada > estoque:
            print(f" Erro: Quantidade indisponivel! voce tentou retirar {retirada}, mas há apenas {estoque} no estoque.")
        else:
                estoque -= retirada
                print(f" Retirada efetuada com sucesso restam {estoque} unidade(s).")

    except ValueError:
        print(" Entrada invalida, por favor! Digite apenas numeros inteiros.")

    print("\n" + "=" * 45)
    print("    ESTOQUE ESGOTADO - OPERAÇÃO ENCERRADA    ")
    print("=" * 45)

    input("\nPressione Enter para encerrar o programa...")
                
                     