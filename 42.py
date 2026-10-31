"""Compara o número de comparações da busca linear e da busca binária."""


def busca_linear(numeros: list[int], alvo: int) -> tuple[int, int]:
    """Retorna o índice encontrado (ou -1) e a quantidade de comparações."""
    comparacoes = 0

    for indice, numero in enumerate(numeros):
        comparacoes += 1
        if numero == alvo:
            return indice, comparacoes

    return -1, comparacoes


def busca_binaria(numeros: list[int], alvo: int) -> tuple[int, int]:
    """Busca em lista ordenada e conta cada comparação com o valor procurado."""
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


def ler_inteiro() -> int:
    """Solicita um número inteiro e repete a leitura se a entrada for inválida."""
    while True:
        try:
            return int(input("Digite o número inteiro que deseja localizar: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def mostrar_resultado(nome: str, indice: int, comparacoes: int) -> None:
    if indice == -1:
        print(f"{nome}: número não encontrado.")
    else:
        print(f"{nome}: número encontrado na posição {indice + 1}.")
    print(f"  Comparações: {comparacoes}")


def main() -> None:
    numeros = [
        3, 7, 12, 18, 21, 26, 30, 34, 39, 43,
        48, 52, 57, 61, 66, 70, 75, 81, 88, 94,
    ]

    print("=== Comparação entre busca linear e busca binária ===")
    print(f"Lista ordenada: {numeros}")
    alvo = ler_inteiro()

    indice_linear, comparacoes_lineares = busca_linear(numeros, alvo)
    indice_binario, comparacoes_binarias = busca_binaria(numeros, alvo)

    print(f"\nValor procurado: {alvo}")
    mostrar_resultado("Busca linear", indice_linear, comparacoes_lineares)
    mostrar_resultado("Busca binária", indice_binario, comparacoes_binarias)


if __name__ == "__main__":
    main()