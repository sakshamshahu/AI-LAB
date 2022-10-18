import numpy as np
a= np.array([1,2,3],dtype='int32')
print(a)
print(a.itemsize*a.size)
b= np.array([[5.0,6.3,5.9],[6,45,3]])
print(b)
print(b.ndim)
print(b.dtype)

r1= np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])
print(r1.shape)
print(r1[1,5])
print(r1[0])
print(r1[:,3])

#[startindex:endindex:stepsize]
print(r1[0,0:7:2])
print(r1[0,0:-1:2])

#3-D array
a1= np.array([[[1,2],[3,4],[5,6]],[[7,8,],[9,10],[11,12]]])
print(a1)
print(a1[0,2,1])
print(a1[:,1,:])
a1[:,1,:] =[[77,88],[55,33]]
print(a1)

#np.zeros && np.ones for constructing matrix of only zeroees and ones
x=np.full((3,3),12) #np.full((shape),NumberToBeInserted,dtype='')
print(x)

x=np.full((a1.shape),44)
print(x)

#Random Decimal Number generation
t=np.random.rand(3,3)
print(t)

#Random Integer Number generation
t=np.random.randint(-7,4,size=(3,3))
print(t)

t=np.identity(4,dtype='int16')
print(t)

#Repeat an array 
arr=np.array([[1,2,3,4]])
t=np.repeat(arr,3,axis=1)
print(t)

NEW= np.ones((5,5),dtype='int16')
print(NEW)
NEW2= np.zeros((3,3),dtype='int16')
print(NEW2)
NEW2[1,1]= 9
print(NEW2)
NEW[1:4,1:4]=NEW2
print(NEW)

'''
You can Use mathematical tools like finding the values of sine and cosine
np.sin && np.cos   etc.
'''
t1=np.array([1,2,3])
print(t1)
print(t1**3)

#Matrix Multiplication
a = np.ones((2,4))
print(a)

b = np.full((4,3),3)
print(b)
print(np.matmul(a,b))

#Find the Determinant
c =np.identity(3)
f=np.linalg.det(c)
print(f)

print(a1)
d=a1.flatten()
print(d)

#Vertically Stacking vectors
v1 =np.array([1,2,3,4])
v2 =np.array([5,6,7,8])
NewV=np.vstack([v1,v2,v2,v1])
print(NewV)