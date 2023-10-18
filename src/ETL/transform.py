"""modulo com todas as transformações necessárias para consolidar os dados de entrada."""

import pandas as pd
from typing import List

def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    '''
    Função para transformar uma lista de dataframes
    em um único dataframe.

    Args:
        data_frame_list (List[pd.DataFrame]): lista de dataframes.

    Returns:
        pd.DataFrame: dataframe
    '''
    return pd.concat(data_frame_list, ignore_index=True)