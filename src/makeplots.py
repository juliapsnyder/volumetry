import os

import typer

from file_extractor import FileInfoExtractor
from file_processor import FileProcessor
from folder_processor import FolderProcessor


def process_single_file(file_path: str):
    """Processes a single file given its path."""
    filename = os.path.basename(file_path)
    mouse_id, timepoint = FileInfoExtractor.extract_info_from_filename(filename)
    if mouse_id and timepoint:
        processor = FileProcessor(file_path, timepoint)
        df = processor.read_and_process()
        if not df.empty:
            print(df)
        else:
            print("Failed to process the file.")
    else:
        print("Could not extract mouse ID and timepoint from filename.")


def process_folder(folder_path: str):
    """Processes all .txt files within a specified folder."""
    folder_processor = FolderProcessor(folder_path)
    folder_processor.process()
    print(f"Processed all files in {folder_path}")


app = typer.Typer()


@app.command()
def file(file_path: str):
    """CLI command to process a single file."""
    process_single_file(file_path)


@app.command()
def folder(base_path: str):
    """CLI command to process all folders in the given base path."""
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path):
            process_folder(folder_path)


if __name__ == "__main__":
    app()
