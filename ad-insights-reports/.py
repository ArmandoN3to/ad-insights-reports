import requests

url = f"https://sidebar.stract.to/api/insights?platform=meta_ads&account=cf76cf576fc567fc56fc5c6f5cf67fc6&token=ProcessoSeletivoStract2025"
headers = {
    "Authorization": "Bearer ProcessoSeletivoStract2025",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())