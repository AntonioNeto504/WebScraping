import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import psycopg2
from psycopg2 import sql

def con_bancoDados():
    try:
        conn = psycopg2.connect(
            dbname='Criptomoedas',
            user='postgres',
            password='aluno',
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabela():
    conn = con_bancoDados()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS cotacoes (
                    id_transacao SERIAL PRIMARY KEY,
                    moeda VARCHAR(50),
                    preco_atual NUMERIC,
                    data_captura TIMESTAMP
                )
            ''')
            conn.commit()
            cur.close()
            print("Tabela verificada/criada com sucesso!")
        except Exception as e:
            print(f"Erro ao criar a tabela: {e}")
        finally:
            conn.close()

def inserir_dados(df):
    conn = con_bancoDados()
    if conn is not None:
        try:
            cur = conn.cursor()
            valores = [(row['Moeda'], row['Preco_Atual'], row['Data_Captura']) for _, row in df.iterrows()]
            cur.executemany('''
                INSERT INTO cotacoes (moeda, preco_atual, data_captura)
                VALUES (%s, %s, %s)
            ''', valores)
            conn.commit()
            cur.close()
            print(f"{len(df)} registros inseridos com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir os dados: {e}")
        finally:
            conn.close()

moedas = [
    "bitcoin", "ethereum", "ripple", "litecoin", "bitcoin-cash",
    "eos", "binance-coin", "stellar", "cardano", "tether",
    "solana", "polkadot", "dogecoin", "chainlink", "uniswap",
    "avalanche", "tron", "polygon", "shiba-inu", "cosmos",
    "algorand", "vechain", "hedera", "theta-network", "filecoin",
    "monero", "tezos", "aave", "maker", "the-graph",
    "mantle", "decentraland", "axie-infinity", "elrond", "flow",
    "chiliz", "pepe", "kucoin-token", "bitcoin-sv", "dash",
    "neo", "zcash", "enjin-coin", "loopring", "quant",
    "iota", "waves", "gala", "thorchain"
]
criar_tabela()

df_new = pd.DataFrame(columns=['Moeda', 'Preco_Atual', 'Data_Captura'])

for moeda in moedas:
    try:
        url = f'https://coinmarketcap.com/currencies/{moeda}/'
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        html = requests.get(url, headers=headers)
        html.raise_for_status()
        
        soup = BeautifulSoup(html.text, 'html.parser')
        
        price_tag = soup.find('span', attrs={'data-test': 'text-cdp-price-display'})
        if price_tag:
            price = price_tag.text.replace('$', '').replace(',', '')
            price = float(price) 
        else:
            print(f"Preço não encontrado para {moeda}. Pulando...")
            continue
        
        time_now = time.strftime('%Y-%m-%d %H:%M:%S')

        df_new = pd.concat([df_new, pd.DataFrame([{
            'Moeda': moeda,
            'Preco_Atual': price,
            'Data_Captura': time_now
        }])], ignore_index=True)
        
        time.sleep(2)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página da moeda {moeda}: {e}")
    except Exception as e:
        print(f"Erro ao processar a moeda {moeda}: {e}")


print(df_new)

if not df_new.empty:
    inserir_dados(df_new)
else:
    print("Nenhum dado coletado para inserir no banco.")
