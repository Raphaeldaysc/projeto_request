import requests
import base64
import os
from dotenv import load_dotenv
load_dotenv()

class ManipulaRepositorios:
    """
    Classe para manipular repositórios no GitHub.

    Permite criar repositórios e adicionar arquivos utilizando a API do GitHub.

    Attributes:
        username (str): Nome de usuário no GitHub.
        api_base_url (str): URL base da API do GitHub.
        access_token (str): Token de acesso à API do GitHub.
        headers (dict): Cabeçalhos para as requisições HTTP.
    """

    def __init__(self, username):
        """
        Inicializa a classe com o nome de usuário e configurações da API.

        Args:
            username (str): Nome de usuário no GitHub.
        """
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv('TOKEN_ACCESS')
        self.headers = {
            'Authorization': "Bearer " + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def cria_repo(self, nome_repo):
        """
        Cria um novo repositório no GitHub.

        Args:
            nome_repo (str): Nome do repositório a ser criado.
        """
        data = {
            "name": nome_repo,
            "description": "Dados dos repositórios de algumas empresas",
            "private": False
        }
        response = requests.post(
            f"{self.api_base_url}/user/repos",
            json=data,
            headers=self.headers
        )

        print(f'status_code criação do repositório: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        """
        Adiciona um arquivo ao repositório especificado.

        Args:
            nome_repo (str): Nome do repositório.
            nome_arquivo (str): Nome que o arquivo terá no repositório.
            caminho_arquivo (str): Caminho local do arquivo a ser enviado.
        """
        # Codificando o arquivo
        with open(caminho_arquivo, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)

        # Realizando o upload
        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
        data = {
            "message": "Adicionando um novo arquivo",
            "content": encoded_content.decode("utf-8")
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code upload do arquivo: {response.status_code}')


# Instanciando um objeto
novo_repo = ManipulaRepositorios('Raphaeldaysc')

# Criando o repositório
nome_repo = 'linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo)

# Adicionando arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amazon.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')