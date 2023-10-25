"""This module contains functions for the ETL process."""

from .extract import extract_from_excel
from .load import load_excel
from .transform import concat_data_frames


def pipeline_completa(
    input_folder: str, output_folder: str, output_filename: str
) -> None:
    """
    Função ETL: Extrai, transforma e carrega os dados dos arquivos xlsx.

    Args:
        input_folder (str): folderpath of the input.
        output_folder (str): folderpath of the output.
        output_filename (str): filename of the output.

    Returns:
        None

    """
    data = extract_from_excel(input_folder)
    df = concat_data_frames(data)
    msg = load_excel(df, output_folder, output_filename)
    print(msg)
