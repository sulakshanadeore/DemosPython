class Employee:
    #public, protected and private

    def __init__(self,name,salary,):
        self.name=name
        self.salary=salary
    
    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary,bonus):
        super().__init__(name, salary)
        self.bonus=bonus

    def showDetails(self):
         super().showDetails()
         print(f"Bonus: {self.bonus}")
       

emp=Employee("Amit",90000)
print(emp.name) #Accessible everywhere --public

# m=Manager("Jack",90000,10000)
# m.showDetails()