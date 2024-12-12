# -*- coding: utf-8 -*-
import yaml
import pytest
from Types import DataType
from DataReader import DataReader


class YAMLDataReader(DataReader):

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
      Yaml = "- Иванов Иван Иванович:\n" + \
      " математика: 95\n" + \
      " литература: 100\n" + \
      " программирование: 80\n"
        
      data = {
        "Иванов Иван Иванович": [
          ("математика", 95), ("литература", 100), ("программирование", 80)
        ],
      }

      return Yaml, data

    def filepath_and_data(self, file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
      p = tmpdir.mkdir("datadir").join("my_data.yaml")
      p.write_text(file_and_data_content[0], encoding='utf-8')
      return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
      file_content = YAMLDataReader().read(filepath_and_data[0])
      assert file_content == filepath_and_data[1]


