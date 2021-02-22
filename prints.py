from homework1_1 import Student, Mentor, Lecturer, Reviewer
from homework1_1 import average_students_course_score, average_lecturers_course_score

student_1 = Student('Joseph', 'Biden', 'yet_unknown')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']
student_2 = Student('Bill', 'Gates', 'simply_genius')
student_2.courses_in_progress += ['Python', 'Git']

mentor_1 = Mentor('Some', 'Buddy')
mentor_1.courses_attached += ['Python']

reviewer_1 = Reviewer("Bruce", "Wayne")
reviewer_1.courses_attached += ['Python']

lecturer_1 = Lecturer("Вася", "Пупкин")
lecturer_1.courses_attached += ["Python", "Git"]
lecturer_2 = Lecturer("Elon", "Musk")
lecturer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 2)
reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Python', 2)  # первая ошибка в консоли
print(student_1.grades)
reviewer_1.rate_hw(student_2, "Python", 10)
reviewer_1.rate_hw(student_2, "Python", 10)
reviewer_1.rate_hw(student_2, "Painting", 1)  # Билл не записан на курсы рисования... ошибка
print(student_2.grades)

student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Python', 2)
student_1.rate_lecturer(lecturer_1, 'Python', 3)
student_2.rate_lecturer(lecturer_1, 'Python', 2)
student_2.rate_lecturer(lecturer_1, 'Git', 1)
student_2.rate_lecturer(lecturer_1, 'Git', 3)

student_1.rate_lecturer(lecturer_2, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 9)  # Билл снизил оценку Илону за что-то...
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Git', 3)  # эта оценка не пойдет в расчёт, ибо Илон не вёл Git, ошибкааа

print(student_1.rate_l)  # бесполезная вещь - список таких оценок наставил студент1 8 2 3 10 10 10
print(student_2.rate_l)  # а таких студент2 питон - 2 9 10, гит 1 3, ещё один 3 не вошёл

print(lecturer_1.grade_dict)  # такие оценки получил препод Вася
print(lecturer_2.grade_dict)  # такие оценки получил Илон Маск
print(lecturer_1)
print(student_1)
print(student_2)
print(student_1.average_hw < student_2.average_hw)  # True, у Билла дела обстоят гораздо лучше...
print(lecturer_1.average_lection_score < lecturer_2.average_lection_score)  # False - неправда, Илон лучше!

a = average_students_course_score('Python', Student.number)
print(a)  # 2+3+2 у первого +10+10 = 27/5 = 5.4
b = average_lecturers_course_score('Python', Lecturer.number)
print(b)  # стр30-40. 8+2+3+2 = 15  +10+10+10+10+9 = 15+49 = 64 / 9 = 7.1111(1)
# assert abs(a - 5.400) < 10e-3  # тест
# assert abs(b - 7.111) < 10e-3  # тест
c = average_lecturers_course_score('Git', Lecturer.number)
print(c)
