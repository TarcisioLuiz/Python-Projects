import requests

def retorna_dados_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    print(response.status_code)
    print(response.text)
    print(type(response.text))
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep


def retorna_dados_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    dados_pokemon = response.json()
    return dados_pokemon



def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
#    retorna_dados_cep('52030010')
#    dados_pokemon = retorna_dados_pokemon('pikachu')
#    print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('https://www.instagram.com/')
    print(response)