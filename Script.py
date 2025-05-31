import pandas as pd
import os

def juntar_csvs():
    #Corridas: October 2024 Qualifier, September 2024 Qualifier, August 2024 Qualifier, July 2024 Qualifier
    pastas_csvs = [
        "/home/eduarda/deepracer-race-data/raw_data/leaderboards/arn:aws:deepracer:::leaderboard/9408cb9a-3494-48d6-ae18-b03d0f1c5569",
        "/home/eduarda/deepracer-race-data/raw_data/leaderboards/arn:aws:deepracer:::leaderboard/ce788878-0e4e-40d1-9861-264af6efac41",
        "/home/eduarda/deepracer-race-data/raw_data/leaderboards/arn:aws:deepracer:::leaderboard/89c6f916-fa1d-42c7-8200-dbf942541864",
        "/home/eduarda/deepracer-race-data/raw_data/leaderboards/arn:aws:deepracer:::leaderboard/3b1708a2-5d19-436a-a97d-ced81b175573",
    ]

    # Nome do arquivo de saída
    arquivo_saida = "arquivos_juntos.csv"
    caminho_saida = "/home/eduarda/deepracer-race-data/raw_data/leaderboards/" + arquivo_saida

    # Lista para armazenar os DataFrames
    lista_dataframes = []

    # Percorrer apenas as pastas especificadas
    for pasta in pastas_csvs:
        if not os.path.exists(pasta):
            print(f"Pasta não encontrada: {pasta}")
            continue

        for nome_arquivo in os.listdir(pasta):
            if nome_arquivo.endswith(".csv"):
                caminho_arquivo = os.path.join(pasta, nome_arquivo)
                try:
                    df = pd.read_csv(caminho_arquivo)
                    lista_dataframes.append(df)
                except Exception as e:
                    print(f"Erro ao ler o arquivo {caminho_arquivo}: {e}")

    if not lista_dataframes:
        print("Nenhum arquivo CSV encontrado.")
        return

    # Concatenar todos os DataFrames
    df_final = pd.concat(lista_dataframes, ignore_index=True)

    # Salvar na raiz de "leaderboards"
    df_final.to_csv(caminho_saida, index=False)

    print(f"CSV final salvo como {caminho_saida}")
