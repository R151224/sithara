import numpy as np
import matplotlib.pyplot as plt
n=input("Enter number of elements:")
x=[]
for i in range(n):
	a=input("Enter the samples:");
	x.append(a)
print(x)
k=input("Enter the values to be shifted:")
s=[]
if(k<=n):
	for i in range(n):
		s.append(x[i-(1*k)])
	print(s)
	plt.subplot(211)
	plt.stem(x)
	plt.subplot(212)
	plt.stem(s)
	plt.show()
else:
	print("it's not valid shifting value")
 
