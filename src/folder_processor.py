import os

import pandas as pd

from file_extractor import FileInfoExtractor
from file_processor import  FileProcessor
from plot_generator import PlotGenerator

class FolderProcessor:
    """Processes all .txt files within a specified folder."""

    def __init__(self, folder_path: str):
        """Initializes the FolderProcessor with a folder path.

        Args:
            folder_path: The path to the folder containing .txt files to be processed.
        """
        self.folder_path = folder_path

    def process(self) -> None:
        """Processes each .txt file in the specified folder.

        This refactored version breaks down the processing steps into smaller functions
        for better modularity and readability.

        Args:
            folder_path: The path to the folder containing .txt files to be processed.
        """
        data_frames = []
        mouse_id, timepoint = '', ''

        for file in os.listdir(self.folder_path):
            if file.endswith('.txt'):
                file_path = os.path.join(self.folder_path, file)
                mouse_id, timepoint = FileInfoExtractor.extract_info_from_filename(file)
                fileProcessor = FileProcessor(file_path, timepoint)
                df = fileProcessor.process_file()
                data_frames.append(df)
        
        if data_frames:
            merged_df = pd.concat(data_frames, ignore_index=True)
            PlotGenerator.generate(merged_df, self.folder_path, mouse_id)
