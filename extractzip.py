import zipfile
from pathlib import Path

def extract_zip_files(directory, output_path):
    p = Path(directory)
    for f in p.glob('*.zip'):
        with zipfile.ZipFile(f, 'r') as archive:
            archive.extractall(path=output_path)
            print(f"Extracted contents from '{f.name}' to '{output_path}' directory.")
extract_zip_files("C:\GoogleExports", "C:\GExports")