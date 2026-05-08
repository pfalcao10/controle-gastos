import json
import os

# gastos.json fica sempre na raiz do projeto, independente de onde o script é chamado
ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "gastos.json")


def carregar_gastos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar_gastos(gastos):
    with open(ARQUIVO, "w") as f:
        json.dump(gastos, f)


def adicionar_gasto(nome, valor):
    if valor < 0:
        raise ValueError("Valor não pode ser negativo")

    gastos = carregar_gastos()
    gastos.append({"nome": nome, "valor": valor})
    salvar_gastos(gastos)


def listar_gastos():
    return carregar_gastos()


def total_gastos():
    gastos = carregar_gastos()
    return sum(g["valor"] for g in gastos)


def menu():
    while True:
        print("\n1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Total gasto")
        print("4 - Sair")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            valor = float(input("Valor: "))
            adicionar_gasto(nome, valor)
            print("Gasto adicionado!")

        elif op == "2":
            for g in listar_gastos():
                print(g)

        elif op == "3":
            print("Total:", total_gastos())

        elif op == "4":
            break


if __name__ == "__main__":
    menu()
