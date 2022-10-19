class Student:
    def __init__(self,name,id,grades=[]):
        self.name=name
        self.id=id
        self.grades=list(grades)
        self.max_grade=5  
    def print_data (self):
        print(f'the name of student is {self.name} is id:{self.id}  his grades:{self.grades}')
    def add_grade(self,grade):
        if len(self.grades)<self.max_grade:
            self.grades.append(grade)
        else:
            print(f"{self.name} have maximum grades")
    def get_avg(self):
        avg=sum(self.grades)/len(self.grades)
        print(f'his avrege {avg}')
    
