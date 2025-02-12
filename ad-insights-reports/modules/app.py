from fastapi import FastAPI

# Criando uma instância do FastAPI
app = FastAPI()

# Criando um endpoint (rota) que responde a requisições GET
@app.get("/")
def home():
    return {
        "nome": "Armando de Oliveira Gonçalves Neto",
        "email":" armandogoncalves2@hotmail.com",
        "linkedin":'linkedin'
        }
