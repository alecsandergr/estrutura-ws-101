"""Test integration"""

import os
import shutil
import tempfile

import pandas as pd

from src.ETL import pipeline_completa


def test_integration():
    """
    Integration test to check the full functionality of the pipeline.

    This test simulates a real case by creating a temporary directory
    with a sample xlsx file, transforming it and loading it into a temporary
    directory and checks if it works properly.

    """
    with tempfile.TemporaryDirectory() as tmpdir:
        # Configuration of the directories
        input_folder = os.path.join(tmpdir, "input")
        output_folder = os.path.join(tmpdir, "output")
        os.makedirs(input_folder)

        # Create a xlsx file for testing purposes
        sample_data = pd.DataFrame({"A": list(range(1, 11)), "B": list("abcdefghij")})
        sample_filepath = os.path.join(input_folder, "sample.xlsx")
        sample_data.to_excel(sample_filepath, index=False)

        # Execute the function
        pipeline_completa(input_folder, output_folder, "consolidado")

        # Check if the file exists
        output_path = os.path.join(output_folder, "consolidado.xlsx")
        assert os.path.exists(output_path)

        # Check if the generated file is the same as the source
        loaded_data = pd.read_excel(output_path)
        pd.testing.assert_frame_equal(sample_data, loaded_data)
