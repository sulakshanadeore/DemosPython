class Student:
    college="ABC College"

    @classmethod
    def changeCollege(cls,newcollegename):
        cls.college=newcollegename
        # print(cls.college)


s1=Student()
s1.changeCollege("xyz college")
Student.changeCollege("pqr college")
print(s1.college)