import json
import os
import requests

ARQUIVO = "gastos.json"
API_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"


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
        raise ValueError("Valor nao pode ser negativo")

    gastos = carregar_gastos()
    gastos.append({"nome": nome, "valor": valor})
    salvar_gastos(gastos)


def listar_gastos():
    return carregar_gastos()


def total_gastos():
    gastos = carregar_gastos()
    return sum(g["valor"] for g in gastos)


def buscar_cotacoes(api_url=API_URL):
    """Busca cotacoes de moedas na AwesomeAPI."""
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        dados = response.json()
        usd = float(dados["USDBRL"]["bid"])
        eur = float(dados["EURBRL"]["bid"])
        return {"USD": usd, "EUR": eur}
    except requests.RequestException:
        return None
    except (KeyError, ValueError):
        return None


def exibir_cotacoes():
    """Exibe as cotacoes atuais de USD e EUR em BRL."""
    print("\nBuscando cotacoes...")
    cotacoes = buscar_cotacoes()
    if cotacoes:
        print(f"  Dolar (USD): R$ {cotacoes['USD']:.2f}")
        print(f"  Euro  (EUR): R$ {cotacoes['EUR']:.2f}")
        total = total_gastos()
        if total > 0:
            print(f"\nSeu total de R$ {total:.2f} equivale a:")
            print(f"  USD $ {total / cotacoes['USD']:.2f}")
            print(f"  EUR  E {total / cotacoes['EUR']:.2f}")
    else:
        print("  Nao foi possivel obter as cotacoes no momento.")


def menu():
    print("\nControle de Gastos")
    while True:
        print("\n1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Total gasto")
        print("4 - Ver cotacoes (USD/EUR)")
        print("5 - Sair")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            valor = float(input("Valor (R$): "))
            adicionar_gasto(nome, valor)
            print("Gasto adicionado!")

        elif op == "2":
            gastos = listar_gastos()
            if not gastos:
                print("Nenhum gasto registrado.")
            else:
                print("\nSeus gastos:")
                for g in gastos:
                    print(f"  - {g['nome']}: R$ {g['valor']:.2f}")

        elif op == "3":
            print(f"\nTotal gasto: R$ {total_gastos():.2f}")

        elif op == "4":
            exibir_cotacoes()

        elif op == "5":
            print("Ate logo!")
            break


if __name__ == "__main__":
    menu()
