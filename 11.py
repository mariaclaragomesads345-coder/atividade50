while True:
    senha = input("Digite a senha: ")

    if senha == "python123":
        print("acesso autorizado")
        break #interrompe o loop
    else:
        print("Senha incorreta. tente novamente")