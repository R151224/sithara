import numpy as np
import matplotlib.pyplot as plt
#w=np.linspace(-4*np.pi,4*np.pi,1000)
n1=input("Enter the number of samples:")
x=[]
for i in range(n1):
	xx=input("Enter the samples:")
	x.append(xx)
print(x)
p=input("Enter the dft points:")
for j in range(p-n1):
	x.append(0)
print(x)
X=[]
mag=[]
phase=[]
for k in range(len(x)-1):
	s=0
	for n in range(len(x)-1):
		s+=x[n]*np.exp(-2*1j*np.pi*k*n/(len(x)))
	X.append(s)
	mag.append(abs(X[k]))
	phase.append(np.angle(X[k]))
#print(X)
plt.subplot(311)
plt.plot(X)
plt.subplot(312)
plt.plot(mag)
plt.subplot(313)
plt.plot(phase)
plt.show()
