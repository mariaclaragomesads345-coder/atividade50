print("=== Sistema de autenticação (acesso restrito) ===")

SENHA_CORRETA = "1234"

MAX_TENTATIVAS = 3

tentativas_realizadas = 0

while tentativas_realizadas < MAX_TENTATIVAS:
    tentativas_restantes = MAX_TENTATIVAS - tentativas_realizadas

    print(f"\n Tentativa {tentativas_realizadas + 1} de {MAX_TENTATIVAS} (Restantes: {tentativas_restantes})")

    senha_digitada = input("Digite a senha: ")

    if senha_digitada == SENHA_CORRETA:
        print("\n" + "=" * 45)
        print(" ACESSO PERMITIDO! Bem-vindo ao sistema. ")
        print("=" * 45)
        break

    else:
        print("\n" + "=" * 55)
        print(" ACESSO BLOQUEADO! Numero maxima de tentivas excedido.")
        print("=" * 55)