import numpy as np
import matplotlib.pyplot as plt
n=input("Enter number of samples:")
x=[]
for i in range(n):
	a=input("Enter the samples:")
	x.append(a)
print(x)
N=input("Enter the N point DFT:")
k=input("Enter the shifting value:")
a=[]
b=[]
for i in range(n):
	if((N+((n-1)-k))<n):
		d=x[N+((n-1)-k)]
		a.append(d)
print(a)
	'''if((N+((n-1)-k))>n):
		b.append(x[N+((n-1)-k)-n])
	print(b)	
	#s.append(d)
#print(s)'''


