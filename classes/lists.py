from random import randint

from .objects.Student import Student
from .objects.Assignment import Assignment
from .objects.Classroom import Classroom
from .objects.Course import Course
from .objects.Student import Student

class Lists(object):
    def __init__(self):
        self.idFailCount = 0
        self.createStudentsList()


    def createStudentsList(self):
        students = []
        for i in range(1 , 20):
            students.append(Student(self.generateID(), "Shay", "Natan", "Humanities", "Philosophy", "In Progress"))
            students.append(Student(self.generateID(), "Gadi", "Sason", "Humanities", "Philosophy", "In Progress"))
            students.append(Student(self.generateID(), "Bill", "DOlentony", "Humanities", "Philosophy", "In Progress"))
            students.append(Student(self.generateID(), "David", "Telby", "Humanities", "History", "In Progress"))
            students.append(Student(self.generateID(), "Jimmy", "Parso", "Humanities", "History", "In Progress"))
            students.append(Student(self.generateID(), "Igal", "Sason", "Humanities", "History", "In Progress"))

        self.students = students


    def generateID(self):
        range_start = 10 ** (9 - 1)
        range_end = (10 ** 9) - 1

        while (True):
            id = randint(range_start, range_end)

            if (self.validateID(id)):
                return id
            print('{}'.format(self.idFailCount))
            self.idFailCount += 1
    def validateID(self, id: int):
        validateDigit = id % 10
        numStep1 = id // 10;
        sum = 0
        counter = 0

        while numStep1 > 0:
            counter += 1
            currDigit = numStep1 % 10
            numStep1 = numStep1 // 10;
            numToAdd = 0



            if (counter % 2 == 0):
                numToAdd = currDigit
            else:
                numToAdd = currDigit * 2

            if (numToAdd > 9):
                sum += numToAdd % 10
                numToAdd = numToAdd // 10

            sum += numToAdd

        if (sum % 10 == 0):
            return validateDigit == 0
        else:
            return ((sum % 10) + validateDigit) == 10
