
from .utils import generateID
from .objects.Assignment import Assignment
from .objects.Classroom import Classroom
from .objects.Course import Course
from .objects.Student import Student

class Lists(object):
    def __init__(self):
        self.createStudentsList()
        self.createCoursesList()
        self.createAssignmentsList()
        self.createClassroomsList()

    def createStudentsList(self):
        students = []
        for i in range(1 , 20):
            students.append(Student(generateID(), "Shay", "Natan", "Humanities", "Philosophy", "In Progress"))
            students.append(Student(generateID(), "Gadi", "Sason", "Humanities", "Philosophy", "In Progress"))
            students.append(Student(generateID(), "Bill", "DOlentony", "Humanities", "Philosophy", "In Progress"))
            students.append(Student(generateID(), "David", "Telby", "Humanities", "History", "In Progress"))
            students.append(Student(generateID(), "Jimmy", "Parso", "Humanities", "History", "In Progress"))
            students.append(Student(generateID(), "Igal", "Sason", "Humanities", "History", "In Progress"))

        self.Students = students

    def createClassroomsList(self):
        Classrooms = []
        Classrooms.append(Classroom(101, "Rio", 33, ""))
        Classrooms.append(Classroom(102, "Moscow", 22, ""))
        Classrooms.append(Classroom(103, "Tokyo", 12, ""))
        Classrooms.append(Classroom(104, "Nairobi", 40, ""))
        Classrooms.append(Classroom(105, "Berlin", 35, ""))

        self.Classrooms = Classrooms

    def createCoursesList(self):
        courses = []
        courses.append(Course(1001,"Some demend", "Humanities","Philosophical Aesthetics: An Introduction", 2))
        courses.append(Course(1002, "Some demend", "Humanities", "Philosophy and Linguistics", 2))
        courses.append(Course(1003, "Some demend", "Humanities", "Psychology and Philosophy", 2))
        courses.append(Course(1004, "Some demend", "Humanities", "Physics and Philosophy", 2))
        courses.append(Course(1005, "Some demend", "Humanities", "Europe in the 20th century", 2))
        courses.append(Course(1006, "Some demend", "Humanities", "Vikings", 2))
        courses.append(Course(1007, "Some demend", "Humanities", "France 1774-1794: reform and revolution", 2))
        courses.append(Course(1008, "Some demend", "Humanities", "Contested nation: Germany, 1871-1918", 2))
        courses.append(Course(1009, "Some demend", "Humanities", "Growth of the USA", 2))
        courses.append(Course(1010, "Some demend", "Humanities", "Russia after Stalin", 2))
        self.Courses = courses

    def createAssignmentsList(self):
        Assignments = []
        Assignments.append(Assignment("Homework 1st lecture", 1001))
        Assignments.append(Assignment("Homework 2nd lecture", 1001))
        Assignments.append(Assignment("Homework 3rd lecture", 1001))
        Assignments.append(Assignment("Homework 4th lecture", 1001))
        Assignments.append(Assignment("Final assignment", 1001))
        Assignments.append(Assignment("Homework 1st lecture", 1002))
        Assignments.append(Assignment("Homework 2nd lecture", 1002))
        Assignments.append(Assignment("Homework 3rd lecture", 1002))
        Assignments.append(Assignment("Homework 4th lecture", 1002))
        Assignments.append(Assignment("Final assignment", 1002))
        Assignments.append(Assignment("Homework 1st lecture", 1003))
        Assignments.append(Assignment("Homework 2nd lecture", 1003))
        Assignments.append(Assignment("Homework 3rd lecture", 1003))
        Assignments.append(Assignment("Homework 4th lecture", 1003))
        Assignments.append(Assignment("Final assignment", 1003))
        Assignments.append(Assignment("Homework 1st lecture", 1004))
        Assignments.append(Assignment("Homework 2nd lecture", 1004))
        Assignments.append(Assignment("Homework 3rd lecture", 1004))
        Assignments.append(Assignment("Homework 4th lecture", 1004))
        Assignments.append(Assignment("Final assignment", 1004))
        self.Assignments = Assignments

    def getByTypeAndID(self, type: str, id: int):
        selectedList = []
        if type.lower() == "assignment":
            selectedList = self.Assignments
        elif type.lower() == "classroom":
            selectedList = self.Classrooms
        elif type.lower() == "course":
            selectedList = self.Courses
        elif type.lower() == "student":
            selectedList = self.Students

        res = ()
        for item in selectedList:
            if item.Id == id:
                res = item
                break

        return res