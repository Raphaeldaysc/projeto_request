# 🔍 Análise de Linguagens de Programação nos Repositórios do GitHub

Este projeto automatiza a **extração, transformação e armazenamento (ETL)** de dados de repositórios públicos do GitHub para identificar as linguagens de programação mais utilizadas por grandes empresas como **Amazon, Netflix e Spotify**.

## 🚀 Visão Geral

Através da API oficial do GitHub, o sistema:

1. 🔐 Acessa a API com autenticação via token  
2. 📥 Extrai os repositórios públicos de cada organização  
3. 🧹 Transforma os dados, capturando:
   - Nome do repositório  
   - Linguagem principal  
   - Descrição (se houver)  
4. 📊 Armazena os resultados em **arquivos CSV**  
5. ☁️ Realiza o upload automático desses arquivos para um repositório no GitHub  

## 🧠 Motivação

O projeto teve início a partir de um curso da Alura, mas foi **reformulado, expandido e estruturado** para atender a um fluxo real de engenharia de dados, com boas práticas de programação e automação.

---

## ⚙️ Tecnologias e Ferramentas

- Python 3.12  
- `requests`  
- `pandas`  
- `base64`  
- `dotenv`  
- API REST do GitHub  

---

## 🧱 Estrutura do Projeto

### 📁 `DadosRepositorio`

Classe responsável por:

- Fazer chamadas paginadas à API do GitHub  
- Extrair nomes e linguagens dos repositórios  
- Retornar um DataFrame estruturado  

### 📁 `ManipulaRepositorios`

Classe para:

- Criar repositórios via API  
- Subir arquivos CSV automaticamente com codificação em base64  

---

## 🧪 Exemplo de Output

```bash
Nome: aws-sdk-java, URL: https://github.com/amzn/aws-sdk-java, Linguagem: Java  
Descrição: The Amazon Web Services SDK for Java.  
----------------------------------------  
Nome: ion-java, URL: https://github.com/amzn/ion-java, Linguagem: Java  
Descrição: A Java implementation of Amazon Ion.  
----------------------------------------
## 📁 Arquivos Gerados

- linguagens_amazon.csv
- linguagens_netflix.csv
- linguagens_spotify.csv

Cada arquivo contém:

| repos_names | repos_languages |
|-------------|-----------------|
| aws-sdk-java | Java |
| ion-java | Java |
| aws-cryptographic-sdk | C++ |
| ... | ... |

## 🛠️ Como executar

1. Clone o repositório
2. Instale as dependências
bash
Copiar
Editar
2. Instale as dependências

Extração e transformação de dados com pandas

Automatização de uploads via requests + base64

Estruturação com POO e organização em classes reutilizáveis

🧑‍💻 Autor
Raphael Dias Câmara
🔗 LinkedIn
📬 rphldev@gmail.com
🌎 Natal, RN — Brasil

📌 Observações
Este projeto foi inspirado no curso da Alura sobre coleta de dados com APIs e Python, mas foi totalmente adaptado, estendido e estruturado para uso prático no contexto de engenharia de dados.
## 🧠 Aprendizados

- Trabalhar com APIs REST reais e autenticação com token
- Paginação e controle de requisições HTTP
- Extração e transformação de dados com pandas
- Automatização de uploads via requests + base64
- Estruturação com POO e organização em classes reutilizáveis

## 🧑‍💻 Autor

- **Raphael Dias Câmara**
- 🔗 [LinkedIn](https://www.linkedin.com/in/raphaeldias/)
- 📬 rphldev@gmail.com
- 🌎 Natal, RN — Brasil
