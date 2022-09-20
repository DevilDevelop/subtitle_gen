from abc import abstractmethod
from os.path import dirname, abspath, join


class Path:
    @abstractmethod
    def root_dir(file_path: str) -> str:
        root_dir = dirname(abspath(__file__))
        return join(root_dir, file_path)

    @abstractmethod
    def change_extension(file_path: str, extension: str) -> str:
        old_extension = file_path.split('.')[-1]
        return f'{file_path[:-len(old_extension)]}{extension}'

