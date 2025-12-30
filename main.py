#  import math_utilities
#ans=math_utilities.add(10,20)
# print(ans)


# print(math_utilities.add(10,100))
#----------------------------------

# from math_utilities import add

# ans=add(10,20)
# print(ans)

# print(add(10,100))
#------------------------------

import math_utilities as mu
import math
import datetime
from datetime import date

m=mu.UserMaths()
print(m.add(10,100))
print(m.subtract(100,90))
print(m.divide(45,5))

sqrtAns=math.sqrt(25)
print(sqrtAns)

print("Factorial = ",math.factorial(3))


a=datetime.datetime.now()
print(a)

b=date.today()
print(b)
c=b.month
print("Month",c)
y=b.year
print("Year=" ,y)
d=b.day
print("Day =" ,d)


my_date=date(2025,12,31)
print(my_date)