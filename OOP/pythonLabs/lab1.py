
# Lab Assignment •   OOP · Introduction to OOP with Python
# Week 1 Lab Assignment — Student, Course & Book Classes
# A graded, submittable lab. Complete the tasks, then check against the model answers and marking guide that follow.
# Submit your .py file(s) with the three classes and a demonstration script, plus the written answers to Task 1. Weight: 100 marks. Estimated time: 2–3 hours.
# 1. Task 1 — Fundamentals (10 marks)
# Answer briefly in your own words:



# 1.	What is the difference between a list and a dictionary?
# In list you can access variables through index, in dictionary you access values through keys
# 2.	What does self represent inside a method?
# A variable that belongs to the class lets say-->   def  setId(self, id): self.id = id







# 2. Task 2 — Book class (25 marks)
# Write a class Book with attributes title, author and pages (set in the constructor), a method is_long() returning True when pages > 300, and a __str__ returning “<title> by <author> (<pages> pp.)”. Create two books and show both methods.
print("----------------------Task 1----------------------------")
class Book:
	def __init__(self, title, author , pages):
		self.title = title
		self.author = author
		self.pages=pages
	def is_long(self):
		return self.pages>300
	def __str__(self):
		return f"{self.title} by {self.author}({self.pages} pp.)"
# ----------------------------------------------------
book1 = Book("Without Pants", "Alex Lesley", 120)
print(book1)  #calling __str__ method
print(book1.is_long()) #false ####### calling second method

book2 = Book("Rich dad , poor dad", "Robert Kyosaki", 400);
print(book2.is_long())# true  ####### calling first method
print(book2) #calling second method




print("-------------------------Task 2-------------------------")


class Student:
    def __init__(self,name):
        self.name = name
        self.grades= []
    def add_grade(self, g):
        self.grades.append(g)
    def average(self):
        if(len(self.grades) <= 0):
            return 0
        sum =0
        for i in self.grades:
            sum+=i
        return sum/len(self.grades)


student = Student("rustam")
student.add_grade(4)
student.add_grade(5)
student.add_grade(4)
print(student.average())










# # 4. Task 4 — Course class (25 marks)
# # Write a class Course with attributes title and capacity, a roster list, an enrol(student) method 
# # that adds a Student when there is space (otherwise prints “Course full”), and a size() method. Create a Course with capacity 2, enrol three students, and show the third is rejected.
print("-------------------------Task 3-------------------------")
class Course:
    def __init__(self, title, capacity,roster):
        self.title = title
        self.capacity = capacity
        self.roster = roster
    def enrol(self,student):
            if(len(self.roster) < self.capacity):
              self.roster.append(student)
            else:
              print("Course full")
    def size(self):
         return len(self.roster)

course1 = Course("Python", 2, [])
course1.enrol("rustam")
course1.enrol("kirill")
course1.enrol("danil")

