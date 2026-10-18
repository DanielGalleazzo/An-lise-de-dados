import requests 
import sys

sys.stdout.reconfigure(encoding="utf-8")

usuario = "DanielGalleazzo"
repositorio = "An-lise-de-dados"
chave_api = ""

headers = {
    "User-Agent": "AppName/1.0",
    "Authorization": f"Bearer {chave_api}"
}

url = f"https://api.github.com/repos/{usuario}/{repositorio}/commits"

params = {
    "author": usuario,
    "since": "2025-11-28T00:00:00Z",
    "until": "2026-10-17T23:59:59Z",
    "per_page": 100
}

response = requests.get(url, headers=headers, params=params)
content = response.text

if response.status_code == 200:
    commits = response.json()
    quantidade = 0 

    for commit in commits:
       
        print(commit["commit"]["message"]) #realmente, fazer essa chamada foi bem mais simples que em C
        quantidade += 1

    print("Quantidade de commits:" , quantidade)
        

else:
    print("Erro:", response.status_code)
    print(response.text)

