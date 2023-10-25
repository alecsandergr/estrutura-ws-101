"""This module contains functions for the ETL process."""

from .extract import extract_from_excel
from .load import load_excel
from .pipeline import pipeline_completa
from .transform import concat_data_frames
