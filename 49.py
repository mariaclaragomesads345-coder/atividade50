"""Controle de estoque com cadastro, busca linear e ordenação alfabética."""


def ler_quantidade() -> int:
    """Solicita uma quantidade inteira não negativa."""
    while True:
        entrada = input("Quantidade inicial: ").strip()
        try:
            quantidade = int(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue

        if quantidade < 0:
            print("A quantidade não pode ser negativa.")
            continue
        return quantidade


def buscar_produto(produtos: list[dict], nome: str) -> dict | None:
    """Procura um produto pelo nome usando busca linear."""
    nome_procurado = nome.strip().casefold()
    for produto in produtos:
        if produto["nome"].casefold() == nome_procurado:
            return produto
    return None


def cadastrar_produto(produtos: list[dict]) -> None:
    while True:
        nome = input("Nome do produto: ").strip()
        if nome:
            break
        print("O nome não pode ficar vazio.")

    produto_existente = buscar_produto(produtos, nome)
    if produto_existente is not None:
        print("Esse produto já está cadastrado. Atualize a quantidade pela opção 2.")
        return

    quantidade = ler_quantidade()
    produtos.append({"nome": nome, "quantidade": quantidade})
    print(f"Produto {nome} cadastrado.")


def atualizar_quantidade(produtos: list[dict]) -> None:
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("O nome não pode ficar vazio.")
        return

    produto = buscar_produto(produtos, nome)
    if produto is None:
        print(f"Produto {nome} não encontrado.")
        return

    quantidade = ler_quantidade()
    produto["quantidade"] = quantidade
    print(f"Estoque de {produto['nome']} atualizado para {quantidade}.")


def listar_produtos(produtos: list[dict]) -> None:
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    # Selection Sort: seleciona o próximo nome em ordem alfabética.
    produtos_ordenados = produtos.copy()
    for indice_atual in range(len(produtos_ordenados) - 1):
        indice_menor = indice_atual
        for indice in range(indice_atual + 1, len(produtos_ordenados)):
            nome_atual = produtos_ordenados[indice]["nome"].casefold()
            nome_menor = produtos_ordenados[indice_menor]["nome"].casefold()
            if nome_atual < nome_menor:
                indice_menor = indice

        if indice_menor != indice_atual:
            produtos_ordenados[indice_atual], produtos_ordenados[indice_menor] = (
                produtos_ordenados[indice_menor],
                produtos_ordenados[indice_atual],
            )

    print("\n=== Estoque em ordem alfabética ===")
    for produto in produtos_ordenados:
        print(f"{produto['nome']}: {produto['quantidade']} unidade(s)")


def pesquisar_produto(produtos: list[dict]) -> None:
    nome = input("Nome do produto que deseja buscar: ").strip()
    if not nome:
        print("O nome da busca não pode ficar vazio.")
        return

    produto = buscar_produto(produtos, nome)
    if produto is None:
        print(f"Produto {nome} não encontrado.")
    else:
        print(f"{produto['nome']}: {produto['quantidade']} unidade(s) em estoque.")


def main() -> None:
    produtos = []

    while True:
        print("\n=== Sistema de controle de estoque ===")
        print("1 - Cadastrar produto")
        print("2 - Registrar quantidade de um produto")
        print("3 - Buscar produto pelo nome")
        print("4 - Listar produtos em ordem alfabética")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            atualizar_quantidade(produtos)
        elif opcao == "3":
            pesquisar_produto(produtos)
        elif opcao == "4":
            listar_produtos(produtos)
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()