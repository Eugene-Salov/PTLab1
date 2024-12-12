from typing import Dict, List, Tuple
# Определение типа данных для студентов
DataType = Dict[str, List[Tuple[str, int]]]


class SearchBestStud:

    def __init__(self, students: DataType) -> None:
        # Инициализация словаря студентов
        self.students = students

    def find_top_student(self) -> None:
        # Флаг, указывающий, найден ли хотя бы один студент
        found = False

        # Поиск студентов, имеющих 90 и более баллов по всем дисциплинам
        for student_name, subjects in self.students.items():
            if all(score >= 90 for _, score in subjects):
                print(f"Студент, имеющий 90 и более баллов по всем",
                      "дисциплинам: {student_name}")
                found = True
                return student_name

        # Если таких студентов нет, выводим сообщение
        if not found:
            print("Нет студентов, имеющих 90 и более баллов",
                  "по всем дисциплинам.")
