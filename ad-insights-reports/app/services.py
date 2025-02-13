import requests
from fastapi import HTTPException
from fastapi.responses import JSONResponse

BASE_URL = "https://sidebar.stract.to"

def get_platforms(token: str):
    """
    Função para consultar as plataformas da API externa.
    """
    url = f"{BASE_URL}/api/platforms"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lança erro se o status não for 200
        return response.json()
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")

def get_accounts(token: str, platform:str):
    url=f"{BASE_URL}/api/accounts?platform={platform}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lança erro se o status não for 200
        return response.json()
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")


def get_insights(token: str, platform: str, account: str):
    url = f"{BASE_URL}/api/insights?platform={platform}&account={account}&token={token}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    # Verificar se a resposta está correta
    if response.status_code != 200:
        raise Exception(f"Erro ao obter insights: {response.text}")

    return response.json()  # Retorna a lista de insights
