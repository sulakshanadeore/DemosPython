import pandas as pd
# s1=pd.Series([10,2,20])
# s2=pd.Series([60,78,80])

# print(s1+s2)

# #works with index(labelnames) and not by position
# s1=pd.Series([10,2,20], index=["A","B","C"])
# s2=pd.Series([60,78,80],index=["C","B","A"])
# print(s1+s2)

# s1=pd.Series([10,20], index=["A","C"])
# s2=pd.Series([60,80],index=["C","A"])
# print(s1+s2)

# #Missing values
# s1=pd.Series([10,2], index=["A","B"])
# s2=pd.Series([60,80],index=["B","C"])
# print(s1+s2)

# s1=pd.Series([10,20,30])
# print("sum=",s1.sum())
# print("Min=",s1.min())
# print("Max=",s1.max())
# print("Average=",s1.mean())


marksSeries=pd.Series([70,80,67])
print(marksSeries)
marksSeries[2]=90 #change value in series
print(marksSeries)
print("------------")
greaterThan70=marksSeries>70 # returns bool
print(greaterThan70)
print("--------")
m=marksSeries[marksSeries>67]  # return values with index matching the condition
print(m)

