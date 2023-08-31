# Gabriela Maria Barbosa Pirauá Cotrim
# Python
# Estrutura de Dados

class ContaBancaria:
    def __init__(self, numero, saldo_inicial=0.0):
        self.numero = numero
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def imprimir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


def main():
    numero_conta = input("Digite o número da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))

    conta = ContaBancaria(numero_conta, saldo_inicial)

    while True:
        print("\nMENU DE OPERAÇÕES:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Imprimir saldo")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor_deposito = float(input("Digite o valor para depósito: "))
            conta.depositar(valor_deposito)
        elif opcao == "2":
            valor_saque = float(input("Digite o valor para saque: "))
            conta.sacar(valor_saque)
        elif opcao == "3":
            conta.imprimir_saldo()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")


if __name__ == "__main__":
    main()
