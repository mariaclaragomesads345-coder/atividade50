"""Ordena dez números inteiros em ordem crescente usando Bubble Sort."""


def bubble_sort(numeros: list[int]) -> None:
    """Ordena a lista recebida sem usar sort() ou sorted()."""
    quantidade = len(numeros)

    for fim in range(quantidade - 1, 0, -1):
        houve_troca = False

        for indice in range(fim):
            if numeros[indice] > numeros[indice + 1]:
                numeros[indice], numeros[indice + 1] = (
                    numeros[indice + 1],
                    numeros[indice],
                )
                houve_troca = True

        if not houve_troca:
            break


def main() -> None:
    numeros = [34, 7, 82, 15, 49, 3, 67, 21, 90, 12]

    print("=== Bubble Sort: ordem crescente ===")
    print(f"Lista original: {numeros}")

    bubble_sort(numeros)

    print(f"Lista ordenada: {numeros}")


if __name__ == "__main__":
    main()