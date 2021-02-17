class Employee:
    def __init__(self,empId,name,marks):
        self.empId=empId
        self.name=name
        self.marks=marks
    def __str__(self):
        return str(self.empId) + self.name + str(self.marks)

listOfEmployees = [Employee(1,'sid',86),Employee(2,'Harish',54),Employee(3,'vishesh',68)]
listOfEmployees.sort(key=lambda x:x.empId)
for i in listOfEmployees:
    print(i)

    