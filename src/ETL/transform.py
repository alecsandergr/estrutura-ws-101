"""modulo com todas as transformações necessárias para consolidar os dados de entrada."""

from typing import List

import pandas as pd


def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função para transformar uma lista de dataframes em um único dataframe.

    Args:
        data_frame_list (List[pd.DataFrame]): lista de dataframes.

    Returns:
        pd.DataFrame: dataframe

    Raises:
        ValueError: if data_frame_list is empty.

    """
    if data_frame_list == []:
        raise ValueError("No data to transform")

    return pd.concat(data_frame_list, ignore_index=True)
