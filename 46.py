"""Ordena uma lista de números inteiros em ordem crescente usando Selection Sort."""


def selection_sort(numeros: list[int]) -> None:
    """Ordena a lista recebida selecionando o menor valor de cada trecho."""
    quantidade = len(numeros)

    for indice_atual in range(quantidade - 1):
        indice_menor = indice_atual

        for indice in range(indice_atual + 1, quantidade):
            if numeros[indice] < numeros[indice_menor]:
                indice_menor = indice

        if indice_menor != indice_atual:
            numeros[indice_atual], numeros[indice_menor] = (
                numeros[indice_menor],
                numeros[indice_atual],
            )


def main() -> None:
    numeros = [34, 7, 82, 15, 49, 3, 67, 21, 90, 12]

    print("=== Selection Sort: ordem crescente ===")
    print(f"Lista original: {numeros}")

    selection_sort(numeros)

    print(f"Lista ordenada: {numeros}")


if __name__ == "__main__":
    main()