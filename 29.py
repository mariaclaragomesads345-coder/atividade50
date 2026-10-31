import random

print("=== Jogo de Ativinhação (numero secreto) ===")
print("Tente advinhar o numero secreto entre 1 e 20!\n")

numero_secreto = random.randint(1, 20)
tentativas = 0

while True:
    try:
        palpite = int(input("Digite seu palpite (1 a 20): "))

        if palpite < 1 or palpite > 20:
            print(" o numero deve estar estritamente entre 1 e 20. tente novamente.\n")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print(" o numero secreto é **maior** do que palpite. tente novamente!\n")
        elif palpite > numero_secreto:
            print(" o numero secreto é **menor** do que o palpite. tente novamente!\n")
        else:
            print("\n" + "=" * 50)
            print(f" PARABÉNS! voce acertou o numero secreto({numero_secreto})!")
            print(f"total de tentativas utilizadas: {tentativas}")
            print("=" * 50)
            break

    except ValueError:
        print("Entrada invalida! por favor, tente novamente digite apenas numeros inteiros.\n")