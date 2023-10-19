"""modulo de extract necessárias para consolidar os dados de entrada."""

import os
import glob
import pandas as pd
from typing import List

def extract_from_excel(path: str) -> List[pd.DataFrame]:
    '''
    Função para ler os arquivos de uma pasta data/input
    e retornar uma lista de dataframes.

    Args: 
        path (str): Caminho da pasta.

    Returns: 
        List[pd.DataFrame]: Lista de dataframes.

    Raises:
        ValueError: Se nao tem arquivos na pasta. 
    '''

    all_files = glob.glob(os.path.join(path, '*.xlsx'))
    if not all_files:
        raise ValueError('No Excel files found in the specified folder')

    data_frame_list = [pd.read_excel(file) for file in all_files]

    return data_frame_list

if __name__ == '__main__':
    path = 'data/input'
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)