# 2) Написать класс, который будет читать .csv любых размеров,
# и будет отдавать ответ построчно аля генератор🤔

from os import path as check_path
from sys import exit


class CsvReader:
    red = '\033[91m'
    white = '\033[0m'

    def __init__(self, path=None):
        if path is not None:
            if check_path.exists(path) and check_path.isfile(path):
                self.path = path
                self.file = open(self.path, 'r')
                self.generator = (line for line in self.file)
            else:
                exit(f"\n{self.red}задайте правильный путь и имя файла{self.white}\n")
        else:
            exit(f"\n{self.red}задайте путь и имя файла{self.white}\n")

    def __del__(self):
        try:
            self.file.close()
        except AttributeError:
            pass

    def __enter__(self):
        self.file = open(self.path, 'r')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def print_next(self, count: int = 1) -> None:
        """печатает count линий из файла если не достигнут конец файла"""

        for counter in range(count):
            try:
                print(next(self.generator), end="")
            except StopIteration:
                print(f"\n\n{self.red}достигнут конец файла!!!\n{self.white}")
                break

    def print_all(self) -> None:
        for line in self.generator:
            print(line, end="")


csv = CsvReader('convertcsv.csv')

with csv:
    print(next(csv.generator).split(","))

csv.print_next(5)
