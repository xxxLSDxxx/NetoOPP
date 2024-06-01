import statistics
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'

    def average_score(self):
        middle_sum =0
        for course_grades in self.grades.values():
            course_sum = []
            for grade in course_grades:
                course_sum.append(grade)
            middle_sum = round(statistics.mean(course_sum),2) 
             
        if middle_sum == 0:
            return f'Студент еще не получал оценки'
        else:
            return f'{middle_sum} '

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        res += f'Средняя оценка за домашние задания: {self.average_score()} \n'
        res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
        res += f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, student):
        if not isinstance(student, Student):
            print(f'Такого студента нет')
            return
        return self.average_score() < student.average_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}


class Lecturer(Mentor):
    def middle_rate(self):
        middle_sum = 0
        for course_grades in self.rates.values():
            course_sum = []
            for grade in course_grades:
                course_sum.append(grade)
            middle_sum = round(statistics.mean(course_sum),2) 
        if middle_sum == 0:
            return f'Оценки еще не выставлялись'
        else:
            return f'{middle_sum }'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        res += f'Средняя оценка {self.middle_rate()}\n'
        return res

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print(f' Такого лектора нет')
            return
        return self.middle_rate() < lecturer.middle_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return res


def grades_students(students_list, course):
    overall_student_rating = 0
    lectors = 0
    for listener in students_list:
        if course in listener.grades.keys():
            average_student_score = []
            for grades in listener.grades[course]:
                average_student_score.append(grades)
            overall_student_rating = round(statistics.mean(average_student_score),2) 
            lectors += 1
            
    if overall_student_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{overall_student_rating}'


def grades_lecturers(lecturer_list, course):
    average_rating = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.rates.keys():
            lecturer_average_rates = []
            for rate in lecturer.rates[course]:
                lecturer_average_rates.append(rate)
            average_rating = round(statistics.mean(lecturer_average_rates),2)
            b += 1
    if average_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{average_rating}'


student_1 = Student('Иван', 'Грозный', 'Male')
student_1.finished_courses = ['Python', 'C++']
student_1.courses_in_progress = ['Git', 'Java']

student_2 = Student('Василий', 'Пупкин', 'Male')
student_2.finished_courses = ['С++', 'Git']
student_2.courses_in_progress = ['Python', 'Java']
students_list = [student_1, student_2]

lecturer_1 = Lecturer('Стивен', 'Сигал')
lecturer_1.courses_attached = ['Git', 'Java']

lecturer_2 = Lecturer('Джеки', 'Чан')
lecturer_2.courses_attached = ['Python']

lecturer_3 = Lecturer('Брюс', 'Ли')
lecturer_3.courses_attached = ['Python']
lecturer_list = [lecturer_1, lecturer_2]

reviewer_1 = Reviewer('Омар', 'Хаян')
reviewer_1.courses_attached = ['Python', 'С++', 'Java', 'Git']

reviewer_2 = Reviewer('Арнольд', 'Шварценегер')
reviewer_2.courses_attached = ['Git', 'Python', 'С++']

reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Java', 5)
reviewer_1.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Python', 2)
reviewer_1.rate_hw(student_1, 'С++', 10)
reviewer_1.rate_hw(student_1, 'С++', 9)
reviewer_1.rate_hw(student_1, 'С++', 4)

reviewer_2.rate_hw(student_2, 'С++', 4)
reviewer_2.rate_hw(student_2, 'С++', 2)
reviewer_2.rate_hw(student_2, 'С++', 3)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 1)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Java', 4)
reviewer_2.rate_hw(student_2, 'Java', 10)

student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Git', 5)
student_1.rate_lecturer(lecturer_1, 'Git', 9)
student_1.rate_lecturer(lecturer_1, 'Java', 6)
student_1.rate_lecturer(lecturer_1, 'Java', 7)
student_1.rate_lecturer(lecturer_1, 'Java', 8)

student_2.rate_lecturer(lecturer_1, 'Java', 10)
student_2.rate_lecturer(lecturer_1, 'Java', 9)
student_2.rate_lecturer(lecturer_1, 'Java', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 2)
student_2.rate_lecturer(lecturer_2, 'Python', 8)

print(student_1)
print(student_2)

if student_1 > student_2:
    print(f'{student_1.name} учится лучше чем {student_2.name}')
else:
    print(f'{student_2.name} учится лучше чем {student_1.name}')

print(reviewer_1)
print(reviewer_2)

print(lecturer_1)
print(lecturer_2)

if lecturer_1 > lecturer_2:
    print(f'{lecturer_1.name, lecturer_1.surname} преподает лучше чем {lecturer_2.name, lecturer_2.surname}')
else:
    print(f'{lecturer_2.name, lecturer_2.surname} преподает лучше чем {lecturer_1.name, lecturer_1.surname}')

print(f'Средняя оценка студентов по курсу "Git": {grades_students(students_list, "Git")}')
print(f'Средняя оценка студентов по курсу "Java": {grades_students(students_list, "Java")}')
print(f'Средняя оценка студентов по курсу "Python": {grades_students(students_list, "Python")}')

print(f'Средняя оценка лекторов по курсу "Git": {grades_lecturers(lecturer_list, "Git")}')
print(f'Средняя оценка лекторов по курсу "Java": {grades_lecturers(lecturer_list, "Java")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(lecturer_list, "Python")}')
