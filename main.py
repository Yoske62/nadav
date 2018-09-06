from classes.lists import Lists

print ("Hello world")

lists = Lists()

for student in lists.students:
    print('{}\t{}\t{}'.format(student.Id, student.FirstName, student.LastName))

