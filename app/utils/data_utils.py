# app/utils/data_utils.py

import pandas as pd

def load_excel_data(file_path, sheet_name="Texts"):
    """
    Load data from an Excel file.

    :param file_path: Path to the Excel file.
    :param sheet_name: Name of the sheet to load.
    :return: DataFrame containing the loaded data.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except Exception as e:
        raise Exception(f"Error loading data from {file_path}: {e}")

def preprocess_text_data(df, text_column="English Text"):
    """
    Preprocess text data from a DataFrame.

    :param df: DataFrame containing the text data.
    :param text_column: Name of the column containing text.
    :return: Concatenated and preprocessed text.
    """
    # Example preprocessing: concatenate text data from a specific column
    concatenated_text = ' '.join(df[text_column].fillna(''))
    return concatenated_text
