#1) install and import numpy

#pip---acronym for packages for python
#it is the package manager for python packages or modules
#Numpy ---Numerical Python: fast numerical calculations and working with arrays (instead of python list)
# How to install---> pip install numpy and then import it

import numpy as np

nums=[1,2,3]
print(nums*2)  # repeats the list

arr=np.array([1,2,3])
print(arr*2)

print(np.zeros(3))
print(np.ones(4))

print(np.arange(1,10,3))

#arr1=np.array([[1,2,3],[4,5,6]])
arr1=np.array([["Anil","Bob","Cindrella"],["Dick","Einstein","Faizen"]])
print("Dimensions of array",arr1.ndim)
print("Row/columns/shape",arr1.shape)
print("size",arr1.size)
print("Data type",arr1.dtype)

#Indexing and Slicing
arr2=np.array([10,20,30,40,50])
print("0th index",arr2[0])# 0th index
print(arr2[1:3])
print("------")
twodim_Arr=np.array([[1,2,3],[4,5,6]])
print(twodim_Arr[1][2])
print("===========")
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b) #[5 7 9]
print(a*b)#[ 4 10 18]
print(a**2)#[1 4 9]
print(b/a)

print("Math funs")
#Common Maths functions
a1=np.array([1,2,3,4])
print(np.sum(a1))
print(np.min(a1))
print(np.max(a1))
print(np.mean(a1))

print("Random nos")
print(np.random.randint(1,100,5))


#Create a array 1-10
#Find sum and average of the above
#reshape/arange into 2x5
#Generate 5 random numbers




