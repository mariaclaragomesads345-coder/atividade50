"""Solicita dez números inteiros e os apresenta em ordem crescente."""


def ler_inteiro(numero: int) -> int:
    """Solicita um número inteiro e repete a leitura se a entrada for inválida."""
    while True:
        try:
            return int(input(f"Digite o {numero}º número inteiro: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def main() -> None:
    numeros = []

    print("=== Ordenação crescente de dez números ===")
    for posicao in range(1, 11):
        numeros.append(ler_inteiro(posicao))

    numeros_ordenados = sorted(numeros)

    print(f"\nNúmeros informados: {numeros}")
    print(f"Em ordem crescente: {numeros_ordenados}")


if __name__ == "__main__":
    main()