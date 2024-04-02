import os

import typer

from folder_processor import FolderProcessor


app = typer.Typer()


def process_folder(folder_path: str):
    """Processes all .txt files within the specified folder."""
    folder_processor = FolderProcessor(folder_path)
    folder_processor.process()
    print(f"Processed all files in {folder_path}")

@app.command()
def main(base_path: str = "data"):
    """Processes all subfolders within the given base path.

    Args:
        base_path (str): The base directory to search for subfolders to process. Defaults to 'data'.
    """
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path):
            process_folder(folder_path)

if __name__ == "__main__":
    app()
