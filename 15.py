votos_1 = 0
votos_2 = 0
votos_3 = 0

print("===Sistema de Votaçao===")
print("Opçao disponiveis: [1], [2], [3]")
print("Digite 'fim' para encerrar a votaçao e ver o resultado.\n")

while True:
    voto = input("Digite o seu voto: ")

    if voto == "fim":
        break
    elif voto == "1":
        votos_1 += 1
    elif voto == "2":
        votos_2 += 1
    elif voto == "3":
        votos_3 += 1
    else:
        print("Opçao inválida! Por favor, digite [1], [2], [3] ou 'fim' para encerrar.")

#exibição dos resultados finais
print("\n" + "=" * 30)
print("Resultados da Votação:")
print(f"Candidato 1: {votos_1} votos")
print(f"Candidato 2: {votos_2} votos")
print(f"Candidato 3: {votos_3} votos")
print("=" * 30)