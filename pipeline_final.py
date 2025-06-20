import pandas as pd
import requests
import os
from dotenv import load_dotenv
load_dotenv()


class DadosRepositorio:
    """Uma classe para interagir com a API do GitHub e recuperar informações de repositórios.

    Esta classe fornece métodos para listar repositórios de um usuário do GitHub, extrair nomes
    e linguagens de repositórios, e criar um DataFrame com os dados coletados.

    Atributos:
        owner (str): Nome de usuário do GitHub do proprietário do repositório.
        api_base_url (str): URL base para requisições à API do GitHub.
        access_token (str): Token de acesso à API do GitHub recuperado das variáveis de ambiente.
        headers (dict): Cabeçalhos HTTP para requisições à API, incluindo autorização e versão.
    """

    def __init__(self, owner):
        """Inicializa a instância DadosRepositorio com o proprietário especificado.

        Args:
            owner (str): Nome de usuário do GitHub do proprietário do repositório.
        """
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv('TOKEN_ACCESS')
        self.headers = {
            'X-GitHub-Api-Version': '2022-11-28',
            'Authorization': f'Bearer {self.access_token}'
        }

    def lista_repositorios(self):
        """Recupera todos os repositórios para o proprietário especificado.

        Realiza requisições paginadas à API do GitHub para buscar todos os repositórios 
        do proprietário. Manipula até 30 páginas com 100 repositórios por página.

        Returns:
            list: Uma lista de páginas, onde cada página é uma lista de dicionários
                 de repositórios da API.
        """
        url = f"{self.api_base_url}/users/{self.owner}/repos"
        repos = []
        for page_num in range(1, 30):
            try:
                page_url = f"{url}?page={page_num}&per_page=100"
                response = requests.get(page_url, headers=self.headers)
                response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
                repos.append(response.json())
            except requests.exceptions.RequestException as e:
                print(f"Erro ao obter a página {page_num}: {e}")
                break
        return repos

    def nomes_repositorios(self, repos):
        """Extrai os nomes dos repositórios da resposta da API.

        Args:
            repos (list): Lista de páginas com dados de repositórios conforme
                         retornado por lista_repositorios().

        Returns:
            list: Lista de nomes de repositórios.
        """
        repos_names = []
        for page in repos:
            for repo in page:
                repos_names.append(repo['name'])
        return repos_names

    def linguagens_repositorios(self, repos):
        """Extrai a linguagem principal de cada repositório da resposta da API.

        Args:
            repos (list): Lista de páginas com dados de repositórios conforme
                         retornado por lista_repositorios().

        Returns:
            list: Lista de linguagens de programação principais para cada repositório.
                 Retorna "Sem linguagem definida" para repositórios sem linguagem.
        """
        repos_languages = []
        for page in repos:
            for repo in page:
                if repo['language'] is not None:
                    repos_languages.append(repo['language'])
                else:
                    repos_languages.append("Sem linguagem definida")
        return repos_languages

    def criar_dataframe(self):
        """Cria um DataFrame pandas com nomes de repositórios e suas linguagens principais.

        Returns:
            pandas.DataFrame: Um DataFrame com nomes de repositórios e suas linguagens principais.
        """
        repos = self.lista_repositorios()
        repos_names = self.nomes_repositorios(repos)
        repos_languages = self.linguagens_repositorios(repos)
        
        df = pd.DataFrame({
            'repos_names': repos_names,
            'repos_languages': repos_languages
        })
        return df


# Coletando e criando DataFrames para diferentes organizações
amazon_repos = DadosRepositorio("amzn")
ling_mais_usadas_amazon = amazon_repos.criar_dataframe()

netflix_repos = DadosRepositorio("netflix")
ling_mais_usadas_netflix = netflix_repos.criar_dataframe()

spotify_repos = DadosRepositorio("spotify")
ling_mais_usadas_spotify = spotify_repos.criar_dataframe()

# Salvando os DataFrames em arquivos CSV
ling_mais_usadas_amazon.to_csv('dados/linguagens_amazon.csv', index=False)
ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv', index=False)
ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv', index=False)


