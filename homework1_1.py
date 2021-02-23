class Student:
    number = []  # добавить все созданные экземпляры в один список

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  # оценки за ДЗ,словарь вида -- курс: список оценок
        self.rate_l = {}  # оценки лектору от студента, словарь вида -- курс: список оценок
        self.average_hw = 0  # средняя оценка ЗА ВСЕ дз у студента
        Student.number.append(self)  # посчитать количество созданных объектов

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if grade in range(11):

                if course in self.rate_l:
                    self.rate_l[course] += [grade]
                else:
                    self.rate_l[course] = [grade]

                if course in lecturer.grade_dict:
                    lecturer.grade_dict[course] += [grade]
                else:
                    lecturer.grade_dict[course] = [grade]

            else:
                print("Оценка только от 1 до 10")
        else:
            print('Ошибкааа')

    def calc_average_hw_score(self):
        grades_list = []
        for value in self.grades.values():
            for each in value:
                grades_list.append(each)
        if grades_list:
            self.average_hw = sum(grades_list) / len(grades_list)

    def __str__(self):
        self.calc_average_hw_score()
        t1 = ', '.join(_ for _ in self.courses_in_progress)
        t2 = ', '.join(_ for _ in self.finished_courses)
        return f'\nИмя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {"{:.1f}".format(self.average_hw)}\n' \
               f'Курсы в процессе изучения: {t1}\n' \
               f'Завершённые курсы: {t2}'

    def __lt__(self, other):
        return self.average_hw < other.average_hw


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    number = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_dict = {}  # это оценки, который получил препод в формате курс: список оценок
        self.average_lection_score = 0  # это среднее значение ЗА ВСЕ его лекции
        self.number.append(self)  # список всех экземляров класса

    def __str__(self):
        self.calc_grade_score()
        return f'\nИмя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {"{:.1f}".format(self.average_lection_score)}'

    def calc_grade_score(self):
        grades_list = []
        for value in self.grade_dict.values():
            for each in value:
                grades_list.append(each)
        if grades_list:
            self.average_lection_score = sum(grades_list) / len(grades_list)

    def __lt__(self, other):
        return self.average_lection_score < other.average_lection_score


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

        else:
            print('Ошибка')

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}'


def average_students_course_score(course: str, students: list):
    average_course_score = []
    for student in students:
        if course in student.grades:
            for each in student.grades[course]:
                average_course_score.append(each)
    if average_course_score:
        return sum(average_course_score) / len(average_course_score)
    return 0


def average_lecturers_course_score(course: str, lecturers: list):
    average_course_score = []
    for lecturer in lecturers:
        if course in lecturer.grade_dict:
            for each in lecturer.grade_dict[course]:
                average_course_score.append(each)
    if average_course_score:
        return sum(average_course_score) / len(average_course_score)
    return 0
