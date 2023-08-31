# Gabriela Maria Barbosa Pirauá Cotrim
# Python
# Estrutura de Dados

class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()

    def elemento_do_topo(self):
        if not self.esta_vazia():
            return self.items[-1]

    def esta_vazia(self):
        return len(self.items) == 0

    def exibir_pilha(self):
        if self.esta_vazia():
            print("A pilha está vazia.")
        else:
            print("Elementos da pilha:", self.items)

    def esvaziar(self):
        self.items = []


def exibir_menu():
    print("\nEDITOR DE LISTAS")
    print("1 - EMPILHAR")
    print("2 - DESEMPILHAR")
    print("3 - EXIBIR ELEMENTO DO TOPO")
    print("4 - EXIBIR A PILHA")
    print("5 - ESVAZIAR A PILHA")
    print("DIGITE SUA OPÇÃO:")


def main():
    pilha = Pilha()
    while True:
        exibir_menu()
        opcao = input()

        if opcao == "1":
            item = int(input("Digite o número a ser empilhado: "))
            pilha.empilhar(item)
        elif opcao == "2":
            item_desempilhado = pilha.desempilhar()
            if item_desempilhado is not None:
                print("Elemento desempilhado:", item_desempilhado)
            else:
                print("A pilha está vazia.")
        elif opcao == "3":
            elemento_topo = pilha.elemento_do_topo()
            if elemento_topo is not None:
                print("Elemento do topo:", elemento_topo)
            else:
                print("A pilha está vazia.")
        elif opcao == "4":
            pilha.exibir_pilha()
        elif opcao == "5":
            pilha.esvaziar()
            print("A pilha foi esvaziada.")
        else:
            print("Opção inválida. Digite uma opção válida do menu.")

if __name__ == "__main__":
    main()