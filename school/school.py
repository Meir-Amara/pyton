from student import Student

class School:
    def __init__(self) :
        self.students=list()
    def add_student(self,student):
        self.students.append(student)
    def print_student_data(self):
        for i in self.students:
            i.print_data()

            
meir=Student("meir",1,[100,90,100])
eden=Student("eden",2,[80,90,70])

# print(meir.name)
    




school=School()
school.add_student(eden)
school.add_student(meir)

school.print_student_data()