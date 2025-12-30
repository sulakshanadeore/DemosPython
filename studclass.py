class Student:
    
    # def __init__(self,name,marks1,marks2):
    #     self.name=name
    #     self.marks1=marks1
    #     self.marks2=marks2

    def calculatemarks(self):
        return self.marks1 + self.marks2
    
    def acceptdata(self):
        self.marks1=int(input("Enter sub1 marks:"))
        self.marks2=int(input("enter sub 2 marks:"))
        
    def add(*nums):
        return sum(nums)
    
    print(add(1,2))
    print(add(1,2,3))
    print(add(1,2,3,4,5))


s1=Student()
s1.acceptdata()
totalmarks=s1.calculatemarks()
print(totalmarks)
# print(s1.name)
# print(s1.marks1)
# print(s1.marks2)
# totalmarks=s1.calculatemarks()
# print(totalmarks)
# print("------")
# s2=Student("Sumit",50,50)
# print(s2.name)
# print(s2.marks1)
# print(s2.marks2)
# totalmarks=s2.calculatemarks();
# print(totalmarks)
