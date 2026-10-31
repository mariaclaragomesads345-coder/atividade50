"""Sistema simples para cadastrar alunos, notas, médias e pesquisar nomes."""


def ler_nota() -> float:
    """Lê uma nota entre 0 e 10, repetindo a pergunta quando inválida."""
    while True:
        try:
            nota = float(input("Digite uma nota de 0 a 10: ").replace(",", "."))
        except ValueError:
            print("Entrada inválida. Digite um valor numérico.")
            continue

        if 0 <= nota <= 10:
            return nota

        print("A nota deve estar entre 0 e 10.")


def cadastrar_aluno(alunos: list[dict]) -> None:
    while True:
        nome = input("Nome do aluno: ").strip()
        if nome:
            break
        print("O nome não pode ficar vazio.")

    notas = [ler_nota()]
    while True:
        continuar = input(
            "Pressione Enter para adicionar outra nota ou digite F para finalizar: "
        ).strip().casefold()
        if continuar == "f":
            break
        if continuar:
            print("Opção inválida. Pressione Enter ou digite F.")
            continue
        notas.append(ler_nota())

    alunos.append({"nome": nome, "notas": notas})
    print(f"Aluno {nome} cadastrado com sucesso.")


def buscar_alunos(alunos: list[dict], nome_procurado: str) -> list[dict]:
    """Localiza linearmente todos os alunos com o nome informado."""
    encontrados = []

    for aluno in alunos:
        if aluno["nome"].casefold() == nome_procurado.strip().casefold():
            encontrados.append(aluno)

    return encontrados


def mostrar_aluno(aluno: dict) -> None:
    notas = aluno["notas"]
    media = sum(notas) / len(notas)
    notas_formatadas = ", ".join(f"{nota:g}" for nota in notas)

    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {notas_formatadas}")
    print(f"Média: {media:.2f}")


def listar_alunos(alunos: list[dict]) -> None:
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n=== Alunos cadastrados ===")
    for numero, aluno in enumerate(alunos, start=1):
        print(f"\nAluno {numero}")
        mostrar_aluno(aluno)


def pesquisar_aluno(alunos: list[dict]) -> None:
    if not alunos:
        print("Nenhum aluno cadastrado para pesquisar.")
        return

    nome = input("Digite o nome do aluno que deseja pesquisar: ").strip()
    if not nome:
        print("O nome da pesquisa não pode ficar vazio.")
        return

    encontrados = buscar_alunos(alunos, nome)
    if not encontrados:
        print(f"Nenhum aluno encontrado com o nome {nome}.")
        return

    print(f"\nEncontrado(s): {len(encontrados)}")
    for aluno in encontrados:
        print()
        mostrar_aluno(aluno)


def main() -> None:
    alunos = []

    while True:
        print("\n=== Sistema de gerenciamento de alunos ===")
        print("1 - Cadastrar aluno e notas")
        print("2 - Listar alunos e médias")
        print("3 - Pesquisar aluno pelo nome")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            pesquisar_aluno(alunos)
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()