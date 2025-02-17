# 🚀 Coletor de Cotações de Criptomoedas

Este projeto tem como objetivo coletar e armazenar os preços atuais de diversas criptomoedas a partir do site [CoinMarketCap](https://coinmarketcap.com/) e inserir esses dados em um banco de dados PostgreSQL.

## 📌 Funcionalidades
- ✅ Conexão com o banco de dados PostgreSQL
- ✅ Criação automática da tabela para armazenar os dados
- ✅ Web scraping dos preços de criptomoedas
- ✅ Armazenamento das cotações no banco de dados
- ✅ Tratamento de erros para garantir a continuidade do processo

## 🛠 Tecnologias Utilizadas
- 🐍 Python
- 🗂 Pandas
- 🌐 Requests
- 🏗 BeautifulSoup
- 🐘 PostgreSQL
- 🔌 Psycopg2

## ▶️ Como Executar

### 1️⃣ Configurar o Banco de Dados
Certifique-se de ter um banco de dados PostgreSQL configurado com as credenciais:
- **📂 Nome do banco:** `Criptomoedas`
- **👤 Usuário:** `postgres`
- **🔑 Senha:** `aluno`
- **🖥 Host:** `localhost`
- **🔌 Porta:** `5432`

Caso queira modificar as credenciais, altere a função `con_bancoDados()` no arquivo principal.

### 2️⃣ Instalar as Dependências
Execute o seguinte comando para instalar as bibliotecas necessárias:
```sh
pip install pandas requests beautifulsoup4 psycopg2
```

### 3️⃣ Executar o Script
Basta rodar o script Python para iniciar o processo de coleta e armazenamento de dados:
```sh
python script.py
```

## 📂 Estrutura do Projeto
```
/
|-- script.py  # 📜 Arquivo principal com toda a lógica do scraping e inserção no banco
|-- README.md  # 📖 Documento explicativo do projeto
```

## 📝 Explicação do Código
1. **🔗 Conexão com o banco de dados**: A função `con_bancoDados()` estabelece a conexão com o PostgreSQL.
2. **🛠 Criação da tabela**: `criar_tabela()` cria a tabela `cotacoes`, caso ainda não exista.
3. **📊 Coleta de dados**:
   - O script percorre uma lista de criptomoedas.
   - Para cada moeda, faz uma requisição HTTP ao CoinMarketCap.
   - Utiliza o BeautifulSoup para extrair o preço atual da moeda.
   - Trata exceções caso ocorra algum erro na extração dos dados.
4. **💾 Armazenamento no Banco**: `inserir_dados(df_new)` insere as cotações no PostgreSQL.

## ⚠️ Observações
- ❗ Caso o site CoinMarketCap mude sua estrutura, pode ser necessário atualizar o seletor usado no BeautifulSoup.
- 🔄 É recomendável rodar o script em intervalos regulares para manter a base de dados atualizada.
- 🔍 Certifique-se de que o banco de dados esteja rodando antes de executar o script.

## 👨‍💻 Autor
Desenvolvido por **Antônio Custódio Neto**.
