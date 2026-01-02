import pandas as pd

data={
    "Name":["Ravi","Amit","Sumit"],
    "Marks":[85,87,90],
    "City":["Pune","Mumbai","Chennai"]
}

data1=pd.DataFrame(data)
print(data1)
print(data1.shape)
print(data1.columns)
print(data1.dtypes)
print("-----Only names columns-------")
print(data1["Name"])
print(data1[["Name","Marks"]])
print(data1[["Name","Marks","City"]])
print("0 the index details: label basedd")
print(data1.loc[0])
print("--------")
print("0, name")
print(data1.loc[0,"Name"])

print("by position")
print(data1.iloc[0])

print("by position 2 records")
print(data1.iloc[0:2])

print("------------")
data1.loc[0,"Marks"]=60
print("changed data")
print(data1)
print("Finding students greater than 60 marks")
data1["result"]=data1["Marks"]>60
print(data1["result"])# gives true/false
print("Actual data=====")
print(data1[data1["result"]]) #give actual data print with true false
print("------------------------------------")
data1["Passed"]=data1["Marks"].astype(int).apply(lambda x:"Pass" if x>80 else "Fail")
# print(data1)
print(data1[["Name","Marks","Passed"]])
# selecteddata=data1[["Name","Marks","Passed"]]
# print(selecteddata)
