from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import sys

# Garante que a pasta src está no path para importar app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# O gastos.json fica na raiz do projeto (um nível acima de src/)
PROJETO_DIR = os.path.dirname(BASE_DIR)
os.chdir(PROJETO_DIR)

from app import adicionar_gasto, listar_gastos, total_gastos, salvar_gastos  # noqa: E402

app = FastAPI(title="Controle de Gastos API")

STATIC_DIR = os.path.join(BASE_DIR, "static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class GastoIn(BaseModel):
    nome: str
    valor: float


@app.get("/")
def index():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


@app.get("/api/gastos")
def get_gastos():
    return listar_gastos()


@app.post("/api/gastos", status_code=201)
def post_gasto(gasto: GastoIn):
    if not gasto.nome.strip():
        raise HTTPException(status_code=400, detail="Nome não pode ser vazio")
    try:
        adicionar_gasto(gasto.nome.strip(), gasto.valor)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"ok": True}


@app.delete("/api/gastos/{index}")
def delete_gasto(index: int):
    gastos = listar_gastos()
    if index < 0 or index >= len(gastos):
        raise HTTPException(status_code=404, detail="Gasto não encontrado")
    gastos.pop(index)
    salvar_gastos(gastos)
    return {"ok": True}


@app.get("/api/total")
def get_total():
    return {"total": total_gastos()}
