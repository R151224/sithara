import numpy as np
import matplotlib.pyplot as plt
n=input("Enter number of samples:")
x=[]
for i in range(n):
	a=input("Enter the samples:")
	x.append(a)
#print(x)
r=[]
r.append(x[0])
for i in range(1,n):
	f=x[(n-1)-(i-1)]
	r.append(f)
#print(r)
plt.subplot(211)
plt.stem(x)
plt.title('signal')
plt.subplot(212)
plt.stem(r)
plt.title('reversed signal')
plt.show()
