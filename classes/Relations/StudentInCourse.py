class StudentInCourse(object):
    def __init__(self, student_id: int, course_id: int, semester: int, year: int):
        self.StudentId = student_id
        self.CourseId = course_id
        self.Semester = semester
        self.Year = year

    def toString(self):
        return "Course: " + self.StudentId + "Semester: " + self.Semester + "/" + self.year