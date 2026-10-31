"""Ordena uma lista de quinze números inteiros em ordem decrescente."""


def main() -> None:
    numeros = [34, 7, 82, 15, 49, 3, 67, 21, 90, 12, 56, 1, 73, 28, 40]

    print("=== Ordenação decrescente ===")
    print(f"Lista original: {numeros}")

    numeros.sort(reverse=True)

    print(f"Lista em ordem decrescente: {numeros}")


if __name__ == "__main__":
    main()