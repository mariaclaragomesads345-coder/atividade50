print("=== Sequencia de Fibonacci (Primeiros 15 termos) ===")

#inicializa os dois primeiros termos da sequencia
termo_anterior = 0
termo_atual = 1

#utiliza a estrutura de repetição
for i in range(1, 16):
    print(f"Termo {i:2d}: {termo_anterior}")

#calcula o proximo termo somando os dois anteriores
    proximo_termo = termo_anterior + termo_atual

#atualiza as variaveis para a proxima interação
    termo_anterior = termo_atual
    termo_atual = proximo_termo