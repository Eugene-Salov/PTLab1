from typing import Dict, List, Tuple
from src.SearchBestStud import SearchBestStud
import pytest
# Определение типа данных для студентов
DataType = Dict[str, List[Tuple[str, int]]]

class TestSearchBestStud:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, str]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 95),
                    ("русский язык", 94),
                    ("программирование", 100),
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        test_student: str = "Абрамов Петр Сергеевич"
        return data, test_student

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      str]) -> None:
        calc_rating = SearchBestStud(input_data[0])
        assert input_data[0] == calc_rating.students

    def test_calc(self, input_data: tuple[DataType, str]) -> None:
        name = SearchBestStud(input_data[0]).find_top_student()
        assert name == input_data[1]