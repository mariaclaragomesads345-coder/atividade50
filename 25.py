"""Analisa as notas de dez alunos: maior, menor e média da turma."""

QUANTIDADE_ALUNOS = 10
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 10.0


def ler_nota(numero_aluno: int) -> float:
    """Lê e valida uma nota no intervalo de 0 a 10, aceitando vírgula decimal."""
    while True:
        entrada = input(f"Digite a nota do aluno {numero_aluno} (0 a 10): ").strip()
        try:
            # Aceita tanto 8.5 quanto 8,5, como é comum em português.
            nota = float(entrada.replace(",", "."))
        except ValueError:
            print("Entrada inválida. Digite um número, por exemplo 7,5.")
            continue

        if not (NOTA_MINIMA <= nota <= NOTA_MAXIMA):
            print("Nota fora do intervalo. Informe um valor entre 0 e 10.")
            continue

        return nota


def main() -> None:
    notas = [ler_nota(aluno) for aluno in range(1, QUANTIDADE_ALUNOS + 1)]

    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / QUANTIDADE_ALUNOS

    print("\n=== Resultado da turma ===")
    print(f"Maior nota: {maior_nota:g}")
    print(f"Menor nota: {menor_nota:g}")
    print(f"Média da turma: {media:.2f}")


if __name__ == "__main__":
    main()