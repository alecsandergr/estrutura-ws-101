"""modulo com todas as transformações necessárias para consolidar os dados de entrada."""

import os
import pandas as pd

def load_excel(dataframe: pd.DataFrame, output_path: str, filename: str) -> str:
    '''
    Recebe um dataframe e salva como excel.

    Args:
        dataframe (pd.DataFrame): dataframe.
        output_path (str): caminho onde o arquivo será salvo.
        filename (str): nome do arquivo.
    Returns:
        'Arquivo salvo com sucesso': mensagem de sucesso.
    '''
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    dataframe.to_excel(f'{output_path}/{filename}.xlsx', index=False)
    return 'Arquivo salvo com sucesso'

