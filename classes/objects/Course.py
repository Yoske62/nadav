class Course(object):
    def __init__(self, course_id: int, pre_demand: str, major: str, course_name: str, academic_points: int):
        self.CourseId = course_id
        self.PreDemand = pre_demand
        self.Major = major
        self.CourseName = course_name
        self.AcademicPoints = academic_points
