"""Tests for unit functionalities."""

import os

import pandas as pd
import pytest

from src.ETL import concat_data_frames, extract_from_excel, load_excel

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
df2 = pd.DataFrame({'A': [4, 5, 6], 'B': ['d', 'e', 'f']})


@pytest.fixture
def mock_input_folder(tmpdir):
    """Fixture to create a mock input folder with xlsx files for testing."""

    input_folder = tmpdir.mkdir('input_folder')
    df1.to_excel(input_folder.join('file1.xlsx'), index=False)
    df2.to_excel(input_folder.join('file2.xlsx'), index=False)

    return str(input_folder)


@pytest.fixture
def mock_output_folder(tmpdir):
    """Fixture to create a mock output folder with xlsx files for testing."""

    return str(tmpdir.mkdir('output_folder'))


@pytest.fixture
def mock_empty_folder(tmpdir):
    """Fixture to create a mock empty folder for testing."""

    return str(tmpdir.mkdir('empty_folder'))


@pytest.fixture
def mock_protected_folder(tmpdir):
    """Fixture to create a mock protected folder for testing."""

    return str(tmpdir.mkdir('protected_folder'))


def test_extract(mock_input_folder):
    """Test the extraction of data from the input folder."""

    extracted_data = extract_from_excel(mock_input_folder)

    assert len(extracted_data) == 2
    assert all(isinstance(df, pd.DataFrame) for df in extracted_data)


def test_extract_no_file(mock_empty_folder):
    """Test the extraction of data from the input folder if no file is provided."""

    with pytest.raises(
        ValueError, match='No Excel files found in the specified folder'
    ):
        extract_from_excel(mock_empty_folder)


# def test_extract_no_files(tmpdir):
#     """Test extraction functionality with an empty input folder."""
#     # Criando uma pasta vazia
#     empty_folder = tmpdir.mkdir("empty_folder")
#     with pytest.raises(ValueError, match="No Excel files found"):
#         extract_excel(str(empty_folder))


def test_transform():
    """Test the transformation of the dataframe."""

    data = [df1, df2]
    conc_df = concat_data_frames(data)

    assert len(conc_df) == 6
    assert list(conc_df.columns) == ['A', 'B']
    assert conc_df['A'].sum() == 21
    assert conc_df['B'].sum() == 'abcdef'


def test_transform_empty_list():
    """Test the transformation if the list is empty."""

    with pytest.raises(ValueError, match='No data to transform'):
        concat_data_frames([])


def test_load(mock_output_folder):
    """Test loading the consolidated data into the output folder."""

    df = pd.concat([df1, df2], axis=0, ignore_index=True)
    output_filename = 'consolidado'
    load_excel(df, mock_output_folder, output_filename)
    path = os.path.join(mock_output_folder, f'{output_filename}.xlsx')

    assert os.path.exists(path)

    loaded_df = pd.read_excel(path)
    pd.testing.assert_frame_equal(loaded_df, df)


def test_load_no_permission(mock_protected_folder):
    """Test load data into a protected folder."""

    os.chmod(mock_protected_folder, 0o444)   # permission to read only

    with pytest.raises(PermissionError):
        load_excel(df1, str(mock_protected_folder), 'test')
