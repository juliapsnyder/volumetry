import pandas as pd


class FileProcessor:
    """Processes individual files to extract relevant data.

    This class reads a file, finds the start of the actual data based on column headers,
    and processes the file to extract relevant data.
    """

    def __init__(self, file_path: str, timepoint: str):
        """Initializes the FileProcessor with file path and timepoint.

        Args:
            file_path: The full path to the file to be processed.
            timepoint: The imaging timepoint to be added as a column.
        """
        self.file_path = file_path
        self.timepoint = timepoint

    @staticmethod
    def find_data_start(file_path: str, column_headers: list) -> int:
        """Finds the line number where actual data starts in the file.

        Args:
            file_path: The path to the file to inspect.
            column_headers: A list of column headers expected at the data start.

        Returns:
            The line number (0-indexed) where the data starts. Returns 0 if not found.
        """
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                if all(header in line for header in column_headers):
                    return i
        return 0

    def process_file(self) -> pd.DataFrame:
        """Reads and processes the file to extract relevant data.

        Returns:
            A pandas DataFrame with 'BinCal', 'Perc_Area', and 'Timepoint' columns. Returns
            an empty DataFrame in case of an error.
        """
        data_start_line = self.find_data_start(self.file_path, ['BinCal', 'Perc_Area'])
        try:
            df = pd.read_csv(self.file_path, sep='\t', skiprows=data_start_line)[['BinCal', 'Perc_Area']]
            df['Timepoint'] = self.timepoint
            return df
        except Exception as e:
            print(f"Error processing file {self.file_path}: {e}")
            return pd.DataFrame()