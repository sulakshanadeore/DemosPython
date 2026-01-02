#install and import pandas
# Pandas is a library to work with tabular data(rows and columns)
#read CSV/Excel files
#clean and analyse data
#SQL _ Excel=pandas
import pandas as pd

#1-D--->Single Column---->Series
#2-D---->Table-------> DataFrame

#NaN-->Not a Number
# s1=pd.Series([10,20,30])
# print(s1)  #index is 0,1,2
            
s=pd.Series([10,20,30],index=['Maths','Science','English'])
# print(s)   #"Maths","Science","English"(labels)

#Always use lables to access data,position will be deprecated in future version
MathsMarksByLabel=s["Maths"]
print("Maths=" ,MathsMarksByLabel)# print/access by label name


print(s[["Maths","English"]])

# MathsMarksByPostion=s[0]
# print("MathsMArks=",MathsMarksByPostion)
