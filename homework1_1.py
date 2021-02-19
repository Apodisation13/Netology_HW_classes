class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.rate_l = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade in range(11):
                self.rate_l.append(grade)
            else:
                print("Оценка только от 1 до 10")
        else:
            print('Ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']

mentor_1 = Mentor('Some', 'Buddy')
mentor_1.courses_attached += ['Python']

reviwer_1 = Reviewer("Bruce", "Wayne")
reviwer_1.courses_attached += ['Python']

lecturer_1 = Lecturer("Elon", "Musk")
lecturer_1.courses_attached += ['Python']

reviwer_1.rate_hw(student_1, 'Python', 7)
reviwer_1.rate_hw(student_1, 'Python', 4)
reviwer_1.rate_hw(student_1, 'Python', 9)


student_1.rate_lecturer(lecturer_1, 'Python', 10)

print(student_1.grades)
print(student_1.rate_l)
