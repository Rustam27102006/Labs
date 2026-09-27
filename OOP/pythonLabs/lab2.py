
#Task 1
class Student:
    _next_id = 1
    _count =0

    def __init__(self, name):
        self.id = Student._next_id
        self.name = name
        self.grades = []
        Student._next_id += 1
        Student._count +=1
    def add_grade(self, g):
        if(g >=0 and g <= 100):
            self.grades.append(g)
    def average(self):
        if(len(self.grades) <=0):
            return 0
        sum = 0
        for i in self.grades:
            sum +=i
        return sum/len(self.grades)
    @classmethod    #Task 2
    def how_many(cls):
        return cls._count

    def __str__(self):
        return f"#{self.id} {self.name} (avg {self.average():.2f})"        






#Task 3
class StudentManager:
    def __init__(self, students):
        self.students = students

    def add(self, name):
        student = Student(name)
        self.students.append(student)
        return student
    def find(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None
    def top_student(self):
        if len(self.students) == 0:
            return None
        top_student = self.students[0]
        for student in self.students:
            if student.average() > top_student.average():
                top_student = student

        return top_student
    def report(self):
        for student in self.students:
            print(student)


student1 = Student("John Wick")
student1.add_grade(90)
student1.add_grade(81)
student2 = Student( "Jane Doe")
student2.add_grade(93)
student2.add_grade(75)
student3 = Student("Alice Smith")
student3.add_grade(89)
student3.add_grade(31)




studentManager =StudentManager([student1, student2, student3])
studentManager.report()
print("Top student:")
print(studentManager.top_student())
print(Student.how_many())

######OUTPUTS########
##1 John Wick (avg 85.50)
##2 Jane Doe (avg 84.00)
##3 Alice Smith (avg 60.00)
# Top student:
##1 John Wick (avg 85.50)
# 3


# Discussion Questions
# 1.	How would you prevent two students from getting the same id?
# To create a class attribute that will belong to everyone (_nextId) . This way we prevent a Student class to call an already existing id. And we should prevent creating a setId method so we don’t change the id.
# 2.	Where would input validation best live — in Student or StudentManager?
# In student cuz it is a domain for creating a student class

