class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

class Student(Person):
    def __init__(self, name, id, grade):
        super().__init__(name, id)
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, id, subject):
        super().__init__(name, id)
        self.subject = subject

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Subject: {self.subject}"

student = Student("Sam", 5678, "B+")
teacher = Teacher("Sha", 1234, "Math")
print(student.get_details())  
print(teacher.get_details())