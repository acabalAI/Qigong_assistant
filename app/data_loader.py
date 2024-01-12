import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        """
        Initializes the DataLoader with the path to the data file.

        :param file_path: Path to the data file.
        """
        self.file_path = file_path

    def load_data(self):
        """
        Loads data from an Excel file.

        :return: DataFrame containing the loaded data.
        """
        try:
            df = pd.read_excel(self.file_path, sheet_name="Texts")
            return df
        except Exception as e:
            raise Exception(f"Error loading data: {e}")

    def preprocess_data(self, df):
        """
        Preprocesses the data for the chatbot.

        :param df: DataFrame containing the raw data.
        :return: Preprocessed text.
        """
        # Example preprocessing: concatenate text data from a specific column
        # Adjust the column name and preprocessing steps as per your data
        concatenated_text = ' '.join(df['English Text'].fillna(''))
        return concatenated_text

    def load_and_process(self):
        """
        Loads and preprocesses the data.

        :return: Preprocessed text ready for the chatbot.
        """
        df = self.load_data()
        preprocessed_text = self.preprocess_data(df)
        return preprocessed_text



