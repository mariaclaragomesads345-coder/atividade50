print("--- VALIDAÇAO DE IDADE ---")

while True:
    try:
        idade = int(input("Digite sua idade: "))

        #valida se a idade esta dentro do intervalo realista (0 a 120 anos)
        if 0 <= idade <= 120:
            print(f"\nIdade valida cadastrada com sucesso: {idade} anos!")
            break # sai do loop quando a idade é valida
        else:
            print("Erro: digite uma idade entre 0 e 120 anos. \n")

    except ValueError:
        print("Erro: digite um numero inteiro valido. \n")
        