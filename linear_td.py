import numpy as np
import matplotlib.pyplot as plt
n1=input("Enter number of samples for x1:")
x1=[]
for i in range(n1):
	a=input("Enter the elements for x1:")
	x1.append(a)
#print(x1)
n2=input("Enter number of samples for x2:")
x2=[]
for i in range(n2):
	a=input("Enter samples for x2:")
	x2.append(a)
#print(x2)
if(n1<n2):
	a=n2-n1
	for i in range(a):
		x1.append(0)
	print(x1)
	print(x2)
elif(n2<n1):
	a=n1-n2
	for i in range(a):
		x2.append(0)
	print(x1)
	print(x2)
x3=np.zeros(len(x1))
#print(x)
for i in range(len(x1)):
	x3[i]=x1[i]+x2[i]
print(x3)
