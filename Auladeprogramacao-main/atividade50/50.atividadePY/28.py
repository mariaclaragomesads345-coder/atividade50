"""Simulação bancária com menu, depósitos, saques e consulta de saldo."""

from decimal import Decimal, InvalidOperation


def ler_valor_positivo(mensagem: str) -> Decimal:
    """Lê um valor monetário positivo com até duas casas decimais."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = Decimal(entrada)
        except InvalidOperation:
            print("Valor inválido. Digite um número, por exemplo 25,50.")
            continue

        if not valor.is_finite():
            print("Valor inválido. Digite um número finito.")
            continue
        if valor <= 0:
            print("O valor deve ser maior que zero.")
            continue
        if valor != valor.quantize(Decimal("0.01")):
            print("Informe no máximo duas casas decimais.")
            continue

        return valor


def exibir_saldo(saldo: Decimal) -> None:
    """Mostra o saldo formatado em reais."""
    print(f"Saldo atual: R$ {saldo:.2f}")


def main() -> None:
    saldo = Decimal("0.00")

    while True:
        print("\n=== SIMULAÇÃO BANCÁRIA ===")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Consultar saldo")
        print("4 - Sair")

        opcao = input("Escolha uma opção (1 a 4): ").strip()

        if opcao == "1":
            valor = ler_valor_positivo("Valor do depósito: R$ ")
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            exibir_saldo(saldo)
        elif opcao == "2":
            if saldo == 0:
                print("Não é possível sacar: o saldo está zerado.")
                continue

            valor = ler_valor_positivo("Valor do saque: R$ ")
            if valor > saldo:
                print("Saque não realizado: saldo insuficiente.")
                exibir_saldo(saldo)
                continue

            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            exibir_saldo(saldo)
        elif opcao == "3":
            exibir_saldo(saldo)
        elif opcao == "4":
            print("Operação encerrada. Obrigado por utilizar a simulação bancária!")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 4.")


if __name__ == "__main__":
    main()
