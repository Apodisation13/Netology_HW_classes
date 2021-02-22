class Student:
    # number = []  # добавить все созданные экземпляры в один список

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  # оценки за ДЗ,словарь вида курс: список оценок
        self.rate_l = {}  # студент ставит оценки преподу за лекцию, словарь типа курс: список оценок
        self.average_hw = 0  # средняя оценка ЗА ВСЕ дз у студента
        # Student.number.append(self)  # посчитать количество созданных объектов, для тренировки

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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_dict = {}
        self.average_lection_score = 0

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
            return 'Ошибка'

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Ruoy', 'Eman', 'yet_unknown')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']
student_2 = Student('Bill', 'Gates', 'female')
student_2.courses_in_progress += ['Python', 'Git']

mentor_1 = Mentor('Some', 'Buddy')
mentor_1.courses_attached += ['Python']

reviwer_1 = Reviewer("Bruce", "Wayne")
reviwer_1.courses_attached += ['Python']

# lecturer_1 = Lecturer("Elon", "Musk")
# lecturer_1.courses_attached += ['Python']
lecturer_1 = Lecturer("Вася", "Пупкин")
lecturer_1.courses_attached += ["Python", "Git"]

reviwer_1.rate_hw(student_1, 'Python', 7)
reviwer_1.rate_hw(student_1, 'Python', 4)
reviwer_1.rate_hw(student_1, 'Python', 9)
print(student_1.grades)

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 2)
student_2.rate_lecturer(lecturer_1, 'Git', 1)

print(student_1.rate_l)
print(student_2.rate_l)

print(lecturer_1.grade_dict)
print(lecturer_1)
print(student_1)
print(student_2)
