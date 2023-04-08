class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    def emp_pay(self):
        return self.pay

    def email(self):
        return "{}.{}@gmail.com".format(self.first_name, self.last_name)


class Developer(Employee):

    def __init__(self, first_name, last_name, pay, program):
        super().__init__(first_name, last_name, pay)
        self.program = program

    def display(self):
        print(self.fullname())
        print(self.emp_pay())
        print(self.email())
        print(self.program)


e1 = Developer("Gopinatha", "N", 50000, "paython")
e1.display()
print([1, 2, 3] * 3)
