#Rule: The default parameters must come at the last
# def greet(name,message="Good day"):
#     print(message,name)


# greet("John","good morning")
# greet("Hari")


# def studentDetails(name,age,city):
#         print(name,city,age)

# #call using parameter names
# studentDetails(name="Jay",city="Mumbai",age=12)
# studentDetails(age=11,name="Jayesh",city="Bangalore")


# def userdetails(username,role="Admin"):
#       print("Hello", username, role)


# userdetails("Grishma")
# userdetails(role="Manager",username="Pari")


# def add(n1,n2):
#     ans=n1+n2
#     return ans

# addans=add(10,20)
# print(addans)


# def calculate(a,b):
#       total=a+b
#       diff=a-b
#       return total,diff

# t,d=calculate(10,3)
# print(t)
# print(d)

# add1=lambda a,b:a+b

# print(add1(100,200))

# square=lambda s: s*s
# print(square(10))

# checkeven=lambda n1:n1%2==0
# print(checkeven(1))


# nums=[10,20,15,5]
# evens=list(map(lambda x: x%2==0,nums))

# # evens=list(filter(lambda x:x%2==0,nums))
# print(evens)

# studs=[("Hari",85),("Gauri",90),("Anita",70)]
# sortedData=sorted(studs, key=lambda x:x[1],reverse=True)
# print(sortedData)


names=["Anusha","Manisha","Barbie","Tina","Mina","Sima"]
print(sorted(names,reverse=True))

