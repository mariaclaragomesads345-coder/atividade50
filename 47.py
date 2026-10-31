"""Ordena uma lista com Insertion Sort e mostra cada etapa."""


def insertion_sort(numeros: list[int]) -> None:
    """Ordena a lista em ordem crescente e exibe o estado após cada inserção."""
    for indice in range(1, len(numeros)):
        valor = numeros[indice]
        posicao = indice - 1

        while posicao >= 0 and numeros[posicao] > valor:
            numeros[posicao + 1] = numeros[posicao]
            posicao -= 1

        numeros[posicao + 1] = valor
        print(f"Após inserir {valor}: {numeros}")


def main() -> None:
    numeros = [34, 7, 82, 15, 49, 3, 67, 21, 90, 12]

    print("=== Insertion Sort: ordem crescente ===")
    print(f"Lista original: {numeros}")
    insertion_sort(numeros)
    print(f"Lista ordenada: {numeros}")


if __name__ == "__main__":
    main()