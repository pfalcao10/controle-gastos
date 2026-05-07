# Controle de Gastos

> **[Acesse a aplicacao publicada aqui](https://SEU-LINK-DO-DEPLOY.vercel.app)**
> *(Substitua pelo link apos fazer o deploy na Vercel)*

## Descricao

O **Controle de Gastos** e uma aplicacao em linha de comando (CLI) desenvolvida para ajudar usuarios a gerenciar suas financas pessoais de forma simples, pratica e eficiente.

A aplicacao permite registrar despesas, visualizar os gastos realizados, acompanhar o total gasto e **consultar as cotacoes atuais de Dolar e Euro** (via API publica), auxiliando na organizacao financeira e na tomada de decisoes mais conscientes.

## Problema

Muitas pessoas enfrentam dificuldades em controlar seus gastos diarios, o que pode levar a falta de planejamento financeiro, endividamento e desorganizacao pessoal.

## Solucao

Este projeto oferece uma solucao simples e acessivel por meio de uma aplicacao CLI que permite:

- Registrar gastos
- Listar despesas cadastradas
- Calcular o total gasto
- **Consultar cotacoes de USD e EUR em tempo real (AwesomeAPI)**
- **Ver o equivalente do total de gastos em moeda estrangeira**

## Publico-alvo

- Pessoas que desejam organizar suas financas pessoais
- Estudantes
- Trabalhadores que precisam controlar seus gastos
- Iniciantes em educacao financeira

## Funcionalidades

- [x] Adicionar novos gastos
- [x] Listar todos os gastos registrados
- [x] Calcular o total de despesas
- [x] Validacao basica de dados
- [x] **Integracao com API de cotacoes (AwesomeAPI) - USD e EUR**

## API Utilizada

**[AwesomeAPI - Cotacoes de Moedas](https://docs.awesomeapi.com.br/api-de-moedas)**

- Endpoint: `https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL`
- Gratuita e sem necessidade de autenticacao
- Retorna a cotacao atual do Dolar e Euro em Reais

## Tecnologias Utilizadas

- Python
- Pytest (testes automatizados)
- Requests (consumo de API)
- GitHub Actions (CI/CD)

## Estrutura do Projeto

```
controle-gastos/
  src/
    app.py           # Logica principal + integracao com API
  tests/
    test_app.py      # Testes unitarios e de integracao
  .github/workflows/
    ci.yml           # Pipeline de CI/CD
  requirements.txt
  README.md
  VERSION
  gastos.json
```

## Como Executar

```bash
# Instalar dependencias
pip install -r requirements.txt

# Rodar a aplicacao
python src/app.py
```

## Testes

```bash
# Rodar todos os testes (unitarios + integracao)
pytest -v
```

## Lint

```bash
flake8 .
```

## Versao

1.1.0

## Autor

Pedro Antonio Falcao de Assis
