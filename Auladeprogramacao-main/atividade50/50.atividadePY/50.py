"""Cadastra e analisa vinte números inteiros por meio de um menu."""


QUANTIDADE_NUMEROS = 20


def ler_inteiro(mensagem: str) -> int:
    """Solicita um número inteiro e repete a leitura se a entrada for inválida."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def cadastrar_numeros() -> list[int]:
    numeros = []
    print(f"Digite {QUANTIDADE_NUMEROS} números inteiros.")

    for posicao in range(1, QUANTIDADE_NUMEROS + 1):
        numero = ler_inteiro(f"{posicao}º número: ")
        numeros.append(numero)

    return numeros


def busca_linear(numeros: list[int], alvo: int) -> tuple[int, int]:
    """Retorna o índice encontrado (ou -1) e as comparações de igualdade."""
    comparacoes = 0

    for indice, numero in enumerate(numeros):
        comparacoes += 1
        if numero == alvo:
            return indice, comparacoes

    return -1, comparacoes


def busca_binaria(numeros: list[int], alvo: int) -> tuple[int, int]:
    """Busca em uma lista ordenada e conta cada comparação com o alvo."""
    inicio = 0
    fim = len(numeros) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2

        comparacoes += 1
        if numeros[meio] == alvo:
            return meio, comparacoes

        comparacoes += 1
        if numeros[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, comparacoes


def mostrar_busca(nome: str, indice: int, comparacoes: int) -> None:
    if indice == -1:
        print(f"{nome}: número não encontrado.")
    else:
        print(f"{nome}: encontrado na posição {indice + 1}.")
    print(f"  Comparações: {comparacoes}")


def main() -> None:
    numeros = cadastrar_numeros()

    while True:
        print("\n=== Análise de números ===")
        print("1 - Calcular média")
        print("2 - Identificar maior e menor número")
        print("3 - Exibir em ordem crescente")
        print("4 - Exibir em ordem decrescente")
        print("5 - Pesquisar por busca linear e binária")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            media = sum(numeros) / len(numeros)
            print(f"Média dos números: {media:.2f}")
        elif opcao == "2":
            print(f"Maior número: {max(numeros)}")
            print(f"Menor número: {min(numeros)}")
        elif opcao == "3":
            print(f"Ordem crescente: {sorted(numeros)}")
        elif opcao == "4":
            print(f"Ordem decrescente: {sorted(numeros, reverse=True)}")
        elif opcao == "5":
            alvo = ler_inteiro("Digite o número que deseja pesquisar: ")
            indice_linear, comparacoes_lineares = busca_linear(numeros, alvo)
            indice_binario, comparacoes_binarias = busca_binaria(
                sorted(numeros), alvo
            )

            print(f"\nNúmero pesquisado: {alvo}")
            mostrar_busca("Busca linear", indice_linear, comparacoes_lineares)
            mostrar_busca("Busca binária", indice_binario, comparacoes_binarias)
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()