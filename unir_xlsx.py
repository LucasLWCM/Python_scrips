import os
import pandas as pd

data_arquivo_folder = 'C:/Caminho/Pasta'  # Este caminho deve ser alterado para um diretório válido
arquivos_carregados = 0

df = pd.DataFrame()  # Inicializa um DataFrame vazio

def read_excel_robust(file_path):
    try:
        # Lê o arquivo Excel usando openpyxl como engine
        df = pd.read_excel(file_path, engine='openpyxl')
    except Exception as e:
        print(f"Erro ao carregar o arquivo {file_path}: {e}")
        return None
    return df

if os.path.exists(data_arquivo_folder):
    for file in os.listdir(data_arquivo_folder):
        file_path = os.path.join(data_arquivo_folder, file)
        if file.endswith('.xlsx'):
            print(f'Carregando arquivo {file}...')
            df_temp = read_excel_robust(file_path)
            if df_temp is not None:
                df = pd.concat([df, df_temp], ignore_index=True)
                arquivos_carregados += 1
            else:
                print(f'Falha ao carregar {file}')

    if not df.empty:
        # Assegura que o caminho onde o arquivo será salvo é válido e acessível
        output_path = os.path.join(data_arquivo_folder, 'C:/Caminho/Pasta/master_store.xlsx')
        df.to_excel(output_path, index=False)
        print(f'Total de arquivos carregados: {arquivos_carregados}')
        print(f'Dados combinados salvos com sucesso em {output_path}.')
    else:
        print('Nenhum arquivo foi carregado.')
else:
    print('Diretório especificado não existe.')
