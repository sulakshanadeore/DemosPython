#1) install openpyxl------->pip install pandas openpyxl
import pandas as pd

# s=pd.read_csv("marks.csv")
# print(s)

s=pd.read_excel("marksData.xlsx")
print(s)
print("---------")
subjectSeries=s["Subjects"]
print(subjectSeries)
print("------")
marksSeries=s["Marks"]
print(marksSeries)
