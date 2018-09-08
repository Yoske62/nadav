from classes.lists import Lists

lists = Lists()

#for student in lists.students:
    #print('{}\t{}\t{}'.format(student.Id, student.FirstName, student.LastName))


print(lists.getByTypeAndID("Classroom", 101).Name)