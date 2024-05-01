import os
import pandas as pd

data_arquivo_folder = 'p1/' #Pasta onde o arquivo está localizado
arquivos_carregados = 0

df = pd.DataFrame()  # Inicializa um DataFrame vazio

def read_csv_robust(file_path):
    try:
        # Tenta ler o arquivo com tratamento para linhas mal formatadas
        df = pd.read_csv(file_path, on_bad_lines='warn')
    except pd.errors.ParserError as e:
        print(f"Erro de análise no arquivo {file_path}: {e}")
        return None
    return df

if os.path.exists(data_arquivo_folder):
    for file in os.listdir(data_arquivo_folder):
        file_path = os.path.join(data_arquivo_folder, file)
        if file.endswith('.csv'):
            print(f'Carregando arquivo {file}...')
            df_temp = read_csv_robust(file_path)
            if df_temp is not None:
                df = pd.concat([df, df_temp], ignore_index=True)
                arquivos_carregados += 1
            else:
                print(f'Falha ao carregar {file}')
        elif file.endswith('.xlsx'):
            print(f'Carregando arquivo {file}...')
            try:
                df_temp = pd.read_excel(file_path, engine='openpyxl')  # 'openpyxl' é para arquivos .xlsx
                df = pd.concat([df, df_temp], ignore_index=True)
                arquivos_carregados += 1
            except Exception as e:
                print(f'Erro ao carregar {file}: {e}')

    if not df.empty:
        df.to_excel('p1/master_store.xlsx', index=False)
        print(f'Total de arquivos carregados: {arquivos_carregados}')
        print('Dados combinados salvos com sucesso.')
    else:
        print('Nenhum arquivo foi carregado.')
else:
    print('Diretório especificado não existe.')
