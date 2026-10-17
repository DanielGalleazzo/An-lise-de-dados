import requests as req 

base = "https://pokeapi.co/api/v2/"
def pokemon_info(nome):
    url = f"{base}/pokemon/{nome}"
    resposta = req.get(url)

    if resposta.status_code == 200:
        informacao_pokemon = resposta.json()
        return informacao_pokemon
        
    else:
        print(f"falhou para retornar {resposta.status_code}")




nome_pokemon = "mewtwo"
nome = nome_pokemon
poke_info = pokemon_info(nome_pokemon)


if poke_info:
    print(f"{poke_info["name"]}")
    print(f"{poke_info["id"]}")
    print(f"{poke_info["height"]}")
    print(f"{poke_info["weight"]}") 