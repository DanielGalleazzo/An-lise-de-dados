import requests 


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
     "since": "2026-08-01T00:00:00Z",
    "until": "2026-10-17T23:59:59Z",
}

response = requests.get(url, headers=headers, params=params)
content = response.text

if response.status_code == 200:
    commits = response.json()

    for commit in commits:
        print(commit["commit"]["message"]) #realmente, fazer essa chamada foi bem mais simples que em C

else:
    print("Erro:", response.status_code)
    print(response.text)

