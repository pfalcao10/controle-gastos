# Controle de Gastos

## Descrição
Aplicação de controle de gastos pessoais com backend FastAPI + Uvicorn e frontend web.

---

## Estrutura do Projeto
```
controle-gastos/
├── src/
│   ├── app.py          # Lógica de negócio
│   ├── api.py          # API REST com FastAPI
│   └── static/
│       └── index.html  # Frontend web
├── tests/
│   └── test_app.py
├── gastos.json
├── requirements.txt
└── README.md
```

---

## Como Executar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Subir o servidor
```bash
cd src
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

### 3. Acessar o frontend
Abra no navegador: http://localhost:8000

---

## Endpoints da API

| Método | Rota              | Descrição                |
|--------|-------------------|--------------------------|
| GET    | /api/gastos       | Lista todos os gastos    |
| POST   | /api/gastos       | Adiciona um novo gasto   |
| DELETE | /api/gastos/{i}   | Remove gasto pelo índice |
| GET    | /api/total        | Retorna o total gasto    |

### Exemplo POST
```json
{ "nome": "Conta de luz", "valor": 230.0 }
```

---

## Testes
```bash
pytest
```

## Autor
Pedro Antônio Falcão de Assis
