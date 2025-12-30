#print("hello world")
# x=10
# print(type(x))
# print(x)
# age=float(input("Enter Age:"))
# print(age)


# x=y=z=100
# print(x)
# print(y)
# print(z)

# z=complex(7,5J)
# print("Real=",  z.real)
# print("Imaginary=", z.imag)

# d=complex(7,5)
# print("Real=",  d.real)
# print("Imaginary=", d.imag)



# numbers=[10,20,30,40]
# print(numbers)
# numbers[0]=99
# print(numbers)
# numbers.append(40)
# numbers.append(50)
# print(numbers)

# datatuple=(10,20,30)
# print(datatuple)


# set_ex={10,20,30,20,30}
# print("printing set: ")
# print(set_ex)
# #set_ex.remove(10)
# set_ex.discard(10)
# set_ex.add(100)
# print(set_ex)

# s1={10,20,30,40}
# s2={20,40}
# s1.difference_update(s2) 
# # removes identical value
# print(s1)


# s={1,2,3,4,5}
# s.difference_update({2,3},{5})
# print(s)

# #difference_update() removes the common elements and updates the same set
# #differenece creates a new set and keeps the original intact

# print("---------")
# a={1,2,3}
# b={2}
# c=a.difference(b)
# print(c)
# print(a)

# student={
# "rollno":1,
# "Studname":"Hari",
# "age":22
# }
# print("Dictionary")
# print(student["rollno"])
# print(student["Studname"])
# print(student["age"])
# print("New Values ---")
# student["Studname"]="John"
# student["rollno"]=100
# print(student["rollno"])
# print(student["Studname"])
# print(student["age"])
# print("After adding city as new key")
# student["city"]="Bangalore"
# student.update({"state":"KA","grade":"A"})
# print(student["rollno"])
# print(student["Studname"])
# print(student["age"])
# print(student["city"])
# print(student["state"])
# print(student["grade"])

# print("-----------------")
# students={
# 1:"Amit",
# 2:"Sumit",
# 3:"Jack"
# }
# marks={}
# sid=int(input("Enter student id: "))
# #mark=int(input("Enter student mark"))
# #marks.setdefault(students[sid],[]).append(mark)
# marks_input=input("Enter student marks separated by space: ")
# marks_list=list(map(int,marks_input.split()))
# marks.setdefault(students[sid],[]).extend(marks_list)
# print(marks)
# #split break string into list by spaces
# #map(int,..) : convert each element into integr
# #extend()--- add multiple values to the list at once
# total=sum(marks_list)
# print("Total marks=", total)
# average=total/len(marks_list)
# print("Average MArks=", average)
# print("-----------------")

# x = int("10")
# print(type(x))
# print(x)
# print()
# y = float(5)
# print(type(y))
# print(y)
# print()
# z = str(100)
# print(type(z))
# print(z)
# print("-----------------")
# x=10
# y=3
# print(x%y)

# num=int(input("Enter number:"))
# if num%2==0:
#     print('Even')
# else:
#     print("Odd")
# print("-----------------")
# print(2 ** 3)
# print("-----------------")
# print(10/3)   
# #Output=3.3333333333333335

# print(10//3)
#Output=3

# x=7
# y=10

# # print(x>5 and y<15)
# print(x>10 and y>15)

# print("-----------------")
# if x>5 and y<15:
#     print(True)
# else:
#     print(False)
# print("-------------------------")
# if x>10 and y>15:
#     print(False)
# else:
#     print(True)

    
# x=True
# print(not x)


# age=20
# has_permission=True

# age>18 and has_permission-Allowed else Not allowed

# # for i=1;i<6;i++
# for i in range(1,6):
#     if i==3:
#         print(i)
#         continue;
#     print(i)

# names=["Amit","Sumit","Jack","Jill","Jim"]
# for n in names:
#     print(n)

# for i in range(5):
#     pass

# age=17
# if age>=18:
#     print("Adult")
# else:
#     pass


def printNosOneToFive():
    i=1
    while i<=5:
        print(i)
        i+=1
    return 0;

printNosOneToFive()

def printnos(start,end):
    i=start
    while i<=end:
        print(i)
        i=i+1
    return 0;

printnos(1,10)

