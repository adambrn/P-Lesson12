""" Создайте класс студента.
* Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
* Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
* Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
* Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых. """

import csv

class NameValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        for item in value.split():
            if not item.isalpha() or not item.istitle():
                raise ValueError(f"{self.name} должно начинатся на заглавную и содержать только буквы")
        instance.__dict__[self.name] = value

class SubjectValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        with open('subjects.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            subjects = next(reader)
            #print(subjects)
            if value not in subjects:
                raise ValueError(f"{value} не верный предмет.")
        instance.__dict__[self.name] = value

class Student:
    name = NameValidator()
    subject = SubjectValidator()

    def __init__(self, name):
        self.name = name
        #self.subject = 'Русский'
        self.subjects_data = {}  # Словарь для хранения данных по предметам

    def add_grade(self, grade):
        if not (2 <= grade <= 5):
            raise ValueError("Оценка должна быть от 2 до 5.")
        if self.subject not in self.subjects_data:
            self.subjects_data[self.subject] = {'grades': [], 'test_results': []}
        self.subjects_data[self.subject]['grades'].append(grade)

    def add_test_result(self, result):
        if not (0 <= result <= 100):
            raise ValueError("Результат должен быть между 0 и 100.")
        if self.subject not in self.subjects_data:
            self.subjects_data[self.subject] = {'grades': [], 'test_results': []}
        self.subjects_data[self.subject]['test_results'].append(result)

    def average_grade(self, subject):
        grades = self.subjects_data.get(subject, {}).get('grades', [])
        return sum(grades) / len(grades)

    def average_test_result(self, subject):
        test_results = self.subjects_data.get(subject, {}).get('test_results', [])
        return sum(test_results) / len(test_results)

    def overall_average_grade(self):
        all_grades = [grade for subject_data in self.subjects_data.values() for grade in subject_data.get('grades', [])]
        return sum(all_grades) / len(all_grades)

    def overall_average_test_result(self):
        all_test_results = [result for subject_data in self.subjects_data.values() for result in subject_data.get('test_results', [])]
        return sum(all_test_results) / len(all_test_results)

if __name__ == "__main__":
    student = Student("Иван Иванов")

    # Добавление оценок
    student.subject = "Русский"
    student.add_grade(4)
    student.add_grade(5)
    student.add_test_result(90)
    student.add_test_result(70)

    # Для другого предмета
    student.subject = "Физика"
    student.add_grade(3)
    student.add_grade(4)
    student.add_test_result(80)
    student.add_test_result(50)

    #student.subject = "Математика"

    # Вывод среднего балла по каждому предмету
    for subject in student.subjects_data.keys():
        print(f"Средний балл в {subject}: {student.average_grade(subject)}")
        print(f"Средний тест в {subject}: {student.average_test_result(subject)}")

    # Вывод общего среднего балла
    print(f"Общий средний балл: {student.overall_average_grade()}")
    print(f"Общий средний тест: {student.overall_average_test_result()}")


