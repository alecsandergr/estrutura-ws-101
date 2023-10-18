"""pipeline principal do projeto."""

from ETL.pipeline import pipeline_completa

def consolida_dados() -> None:
    '''
    Consolida os arquivos xlsx em único arquivo.

    Returns:
        None
    '''

    input_folder = 'data/input'
    output_folder = 'data/output'
    output_filename = 'consolidado'
    pipeline_completa(input_folder, output_folder, output_filename)


if __name__ == '__main__':
    consolida_dados()
