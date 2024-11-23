import os
import shutil
from pathlib import Path
from threading import Thread

from errors import DirectoryNotFoundError


class FileHandler:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(
                f"The file at {self.file_path} does not exist.")

    def copy_file(self, destination_directory: str):
        os.makedirs(destination_directory, exist_ok=True)
        shutil.copy(self.file_path, destination_directory)

    def file_extension(self):
        return self.file_path.suffix[1:]


class DirectoryHandler:
    def __init__(
            self,
            source_directory: str,
            destination_directory: str):

        self.src_dir = Path(source_directory)
        if not self.src_dir.exists() or not self.src_dir.is_dir():
            raise DirectoryNotFoundError(
                f"Directory {source_directory} doesn't " +
                "exist or is not a directory!"
            )

        if destination_directory:
            self.dest_dir = Path(destination_directory)
        else:
            self.dest_dir = Path("dist")

        if not self.dest_dir.exists():
            os.makedirs(self.dest_dir)
            print(f"Created destination directory: {self.dest_dir}")

    def copy_file(self, path):
        file_handler = FileHandler(path)
        extension = file_handler.file_extension()
        extension = extension or "other"
        dest_dir = self.dest_dir / extension
        os.makedirs(dest_dir, exist_ok=True)
        file_handler.copy_file(dest_dir)

    def process_directory(self, directory):
        threads = []
        for item in os.listdir(directory):
            item_path = directory / item
            if item_path.is_file():
                thr = Thread(target=self.copy_file, args=(item_path,))
                thr.start()
                threads.append(thr)
            elif item_path.is_dir():
                thr = Thread(target=self.process_directory, args=(item_path,))
                thr.start()
                threads.append(thr)

        for thr in threads:
            thr.join()
