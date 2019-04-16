import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
wr=[]
m=input("enter no.of samples:")
for n in range(0,m):
	wr=np.append(wr,1)
plt.subplot(2,3,1)
plt.stem(wr)


t=np.arange(0,m,1)
p=[]
for n in range(0,m):
	w=np.abs(n-((m-1)/2.0))
	y=(2.0*w)/(m-1)
	z=1.0-y
	p=np.append(p,z)
plt.subplot(2,3,2)
plt.stem(t,p)

t=np.arange(0,m,1)
p=[]
for n in range(0,m):
	w=np.cos((2*np.pi*n)/(m-1))
	y=0.5*w
	z=0.5-y
	p=np.append(p,z)
plt.subplot(2,3,3)
plt.stem(t,p)
	

t=np.arange(0,m,1)
p=[]
for n in range(0,m):
	w=np.cos((2*np.pi*n)/(m-1))
	y=0.46*w
	z=0.54-y
	p=np.append(p,z)
plt.subplot(2,3,4)
plt.stem(t,p)


t=np.arange(0,m,1)
p=[]
for n in range(0,m):
	w=np.cos((2*np.pi*n)/(m-1))
	x=0.5*w
	y=np.cos((4*np.pi*n)/(m-1))
	z=0.08*y
	q=0.42-x+z
	p=np.append(p,q)
plt.subplot(2,3,5)
plt.stem(t,p)
plt.show()



