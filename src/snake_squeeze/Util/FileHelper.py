from pathlib import Path
from typing import List


class FileHelper(object):

    @staticmethod
    def read_file(file_path) -> List[str]:
        if not file_path.exists():
            raise ValueError(f"Path '{file_path}' doesn't exist")
        with open(str(file_path)) as fp:
            return fp.read().splitlines()

    @staticmethod
    def read_file_as_int(file_path: Path) -> List[int]:
        if not file_path.exists():
            raise ValueError(f"Path '{file_path}' doesn't exist")
        with open(str(file_path)) as fp:
            return [int(i) for i in fp.readlines()]
