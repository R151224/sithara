import numpy as np
import matplotlib.pyplot as plt
sample =input("enter number of samples:")
x = np.arange(sample)
y1=x*x
plt.plot(x,y1,'g')
plt.xlabel('sample(n)')
plt.ylabel('sample(V)')
si=[]
for i in range(0,sample):
	y1=i*i
	si.append(y1)
print(si)
len=len(si)
sum=[]
s2=0
for i in range(0,len):	
		s2 += si[i]
		sum.append(s2)
plt.stem(i,sum)
plt.show()


