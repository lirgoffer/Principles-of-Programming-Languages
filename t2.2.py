#Autor: Lir Goffer. ID:209103274

from functools import reduce

class Course:
    """
     A class to represent a course.
      :argument
        name:str
             name of the course.
        grade:int
             grade of the course.
    """
    def __init__(self, name):
        """
         Constructs all the necessary attributes for the course object.
         :param name: str
        """
        self.name = name
        self.grade = 101

    def setGrade(self, grade):
        """
         set the grade of the course.
         :param grade: int
        """
        if -1 < grade < 101:
            self.grade = grade



class Student:
    """
    A class to represent a student.
    :argument
    name: str
          full name of the student.
    id: long
        id of the student.
    """
    def __init__(self, name, id):
        """
        Constructs all the necessary attributes for the student object.
         :param name: str
         :param id: int
         :param courses: array of courses
        """
        self.name = name
        self.__id = id
        self.courses = []

    def getID(self):
        """
        return the student id.
        :return: id
         """
        return self.__id

    def addCourse(self, course):
        """
         add course to the courses of the student.
         :param course: str
        """
        if -1 < course.grade < 101:
            self.courses.append(course)


def Get_id_grades_string_for_student(student_name_list, student_name):
    """
        get the id and the grades of the student.

        :param student_name_list: student name list
        :param student_name: student name
        :return: string of id and averages
     """
    index = student_name_list.index(student_name)
    grade_list = list(map(lambda course:course.grade, student_list[index].courses))
    grade_sum = reduce(lambda x, y: x + y, grade_list)
    return f"{student_list[index].getID()} {grade_sum/len(grade_list)}\n"


def Cal_st_avg():
    """
    calculate student average.
    :return: none
    """
    print('please enter the student name:')
    name1 = input()
    student_name_list = list(map(lambda student: student.name, student_list))
    if name1 in student_name_list:
        s = Get_id_grades_string_for_student(student_name_list, name1)
        print(s)
    else:
        print('student does not exist')


def Cal_co_avg():
    """
    calculate course average.
    :return: none
    """
    print('please enter the course name:')
    name1 = input()
    course_list = reduce(lambda course_lst1, course_lst2: course_lst1 + course_lst2, map(lambda student: student.courses, student_list))
    relevant_course = list(filter(lambda course: course.name == name1, course_list))
    if relevant_course:
        avg = reduce(lambda grade1, grade2: grade1+grade2, map(lambda course: course.grade, relevant_course)) / len(relevant_course)
        print(name1, avg)
    else:
        print("invalid course name")


def All_st_avg():
    """
    calculate average of all the student and write their id and average to the file.
    :return: none
    """
    print("please enter file name:")
    filename = input()
    student_name_list = list(map(lambda student: student.name, student_list))
    student_avgs = reduce(lambda id_avg1, id_avg2: id_avg1+id_avg2, list(map(lambda student_name: Get_id_grades_string_for_student(student_name_list, student_name), student_name_list)))
    f = open(filename, "w")
    f.write(student_avgs)
    f.close()


print("please enter file name:")
filename = input()
user_input = ''

student_list = []
f = None
try:
    f = open(filename, "r")
except IOError:
    print("filename invalid")

if f:
    for line in f:
        student_data = line.strip().split('\t')
        current_student = Student(student_data[0], student_data[1])
        student_list.append(current_student)
        course_data = student_data[2].split(';')
        course_dict = {}
        for course in course_data:
            name, grade = course.split('#')
            grade = int(grade)
            if name in course_dict:
                if -1 < grade < 101:
                    course_dict[name] = grade
            else:
                course_dict[name] = grade
        for name, grade in course_dict.items():
            current_course = Course(name)
            current_course.setGrade(grade)
            current_student.addCourse(current_course)

    f.close()
else:
    user_input = '4'


func_dict = {'1': Cal_st_avg, '2': Cal_co_avg, '3': All_st_avg, '4': lambda: print('goodbye :)')}
while user_input != '4':
    print("1. Calculate student average\n2. Calculate course average\n3. Calculate all students average\n4. End program")
    user_input = input()
    func_dict[user_input]()