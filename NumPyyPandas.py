import  numpy as np

a=np.array([1,2,3])
print(a)
a=np.arange(0,1000)
a=np.zeros((8))
print(a)
ad=a.reshape((2,2,2))
print(ad)
a=np.linspace(0,20,5)
print(a)
b=np.array([[1,2],[55,66]])
print(b)
arr=np.savetxt("nums.csv",b,delimiter=';')
# arr=np.loadtxt("nums.txt")
arr=np.genfromtxt('nums.csv',delimiter=';')
print(arr)
ba=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ba[0:3,0:2])
#---->Slice(0,20,2)--(start,stop,step)