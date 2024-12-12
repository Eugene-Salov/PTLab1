# -*- coding: utf-8 -*-
import yaml

from Types import DataType
from DataReader import DataReader


class YAMLDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            students = yaml.safe_load(file)
            for student in students:
                key1, value = list(student.items())[0]
                self.students[key1] = []
                for d in value.keys():
                    n = value.get(d)
                    self.students[key1].append((d, n))
        return self.students
