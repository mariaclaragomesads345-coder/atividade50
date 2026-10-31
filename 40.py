print("=== Busca do Menor Valor em Lista (sem min()) ===")

#lista predefinita com exatamente 20 numeros
numeros = [45, 12, 89, 3, 67, 23, 90, 5, 34, 78, 1, 56, 33, 88, 14, 9, 72, 41, 19, 60]

#Inicializa o menor valor e o indice assumindo que o primeiro elemento (índice 0) é o menor
menor_valor = numeros[0]
indice_menor = 0

#percorre a lista a partir do segundo elemento (indice 1) até o final
for i in range(1, len(numeros)):
    #Compara o elemento atual com o menor valor registrado até o momento
    if numeros[i] < menor_valor:
        menor_valor = numeros[i]  #atualiza o menor numero
        indice_menor = i

#apresentação formatada do relatorio final
print(f"\nLista analisada ({len(numeros)} numeros):")
print(numeros)
print("\n" + "=" * 50)
print(f" O menor valor encontrado é: {menor_valor}")
print(f" O índice (posição) na lista é: {indice_menor}")
print("=" * 50)