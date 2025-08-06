class edu():
    def __init__(self):
        self.name = input("Enter Student name :")
        self.clg = input("Enter College name :")
        self.degree = input("Enter Department :") 
        
    def display_details(self):
        print("\n------------Student Detail------------")
        print(f"\tName       :{self.name}")
        print(f"\tCollege    :{self.clg}")
        print(f"\tDepartment :{self.degree}")
stu1 = edu()
stu1.display_details()