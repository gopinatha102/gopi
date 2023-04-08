class Student:
    cname = "REVA"

    """This is Student Class """
    def __init__(self, name, roll_no=20, marks=90):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        self.dss = 100
        print("College Name is {} and Student name is {} and Roll No is {} and Marks is {}".format(Student.cname, self.name, self.roll_no, self.marks))


s1 = Student("gopinatha")
s1.display()
s1.cname=10
s2 = Student("Sunny", 135, 90)
s2.display()
print(s1.__dict__)
print(s2.__dict__)