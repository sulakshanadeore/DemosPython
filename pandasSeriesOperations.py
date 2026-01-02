import pandas as pd
import numpy as np
s=pd.Series([10,20,30],index=['Maths','Science','English'])
# print(s+5)
# print(s*2)
# print(s**2)
# print(s/2)


#Convert the stud_marks dictionary to Series
stud_marks={
    "Maths":10,
    "Science":20,
    "English":30
}
print(stud_marks)
ms=pd.Series(stud_marks)#Converting to series
print(ms)
print("-----------------")
#Convert the array to series
arr=np.array([10,20,30,40])
ArrSeries=pd.Series(arr)
print(ArrSeries)


