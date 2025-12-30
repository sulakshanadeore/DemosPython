class Employee:
    count_Emp=0

    def __init__(self):
        Employee.count_Emp+=1

    @classmethod
    def get_Count(cls):
        return cls.count_Emp
    

e1=Employee()
e2=Employee()

print (Employee.get_Count())