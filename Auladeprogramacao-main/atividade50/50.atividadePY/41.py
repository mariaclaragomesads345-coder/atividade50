"""Realiza uma busca binária em uma lista ordenada de 20 números inteiros."""


def busca_binaria(numeros: list[int], alvo: int) -> int:
    """Retorna o índice do alvo ou -1 se ele não estiver na lista."""
    inicio = 0
    fim = len(numeros) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if numeros[meio] == alvo:
            return meio
        if numeros[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def ler_inteiro() -> int:
    """Solicita um número inteiro e repete a leitura se a entrada for inválida."""
    while True:
        entrada = input("Digite um número inteiro para buscar: ")
        try:
            return int(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def main() -> None:
    numeros = [
        3, 7, 12, 18, 21, 26, 30, 34, 39, 43,
        48, 52, 57, 61, 66, 70, 75, 81, 88, 94,
    ]

    print("=== Busca binária ===")
    print(f"Lista ordenada: {numeros}")
    alvo = ler_inteiro()

    indice = busca_binaria(numeros, alvo)
    if indice == -1:
        print(f"O número {alvo} não foi encontrado na lista.")
    else:
        print(f"O número {alvo} foi encontrado no índice {indice}.")
        print(f"Posição na lista (começando em 1): {indice + 1}.")


if __name__ == "__main__":
    main()