from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from app.services import get_platforms, get_accounts,get_insights
import pandas as pd

# Criando uma instância do FastAPI
app = FastAPI()
TOKEN="ProcessoSeletivoStract2025"

# Criando um endpoint (rota) que responde a requisições GET
@app.get("/")
def home():
    return JSONResponse(content={
        "nome": "Armando de Oliveira Gonçalves Neto",
        "email":" armandogoncalves2@hotmail.com",
        "linkedin":'linkedin'
        })

# @app.get("/accounts")
# def accounts():
#     accounts=get_accounts(TOKEN,"meta_ads")
#     return JSONResponse(content=accounts)

@app.get("/insights")
def insights(plataforma:str):
    accounts=get_accounts(TOKEN,"meta_ads")
    data=get_insights(TOKEN,platform=plataforma,account=accounts['accounts'])
    return JSONResponse(content=data)

# @app.get("/{plataforma}")
# def get_platform_data(plataforma: str):
#     try:
#         # Log para verificar a plataforma
#         print(f"Buscando contas para a plataforma: {plataforma}")
#         accounts = get_accounts(TOKEN, plataforma)  # Função para buscar contas

#         # Log para verificar as contas retornadas
#         print(f"Contas retornadas: {accounts}")

#         data = []
#         for account in accounts:
#             print(f"Buscando insights para a conta: {account['name']}")
#             insights = get_insights(TOKEN, plataforma, account["id"])

#             # Log para verificar os insights retornados
#             print(f"Insights para a conta {account['name']}: {insights}")

#             for insight in insights:
#                 insight["account_name"] = account["name"]
#                 data.append(insight)

#         # Gerar CSV usando pandas
#         df = pd.DataFrame(data)
#         print("DataFrame gerado com sucesso!")

#         csv = df.to_csv(index=False)
#         return StreamingResponse(
#             iter([csv]),
#             media_type="text/csv",
#             headers={"Content-Disposition": f"attachment; filename={plataforma}.csv"}
#         )
#     except Exception as e:
#         # Log do erro
#         print(f"Erro: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))
    

    
