import numpy as np
import matplotlib.pyplot as plt
w=np.linspace(-np.pi,np.pi,500)
#s=c.sqrt(-1)
n1=input('Enter the number of elements:')
x=[]
m=[]
p=[]
for i in range(n1):
	q=input("Enter the samples:")
	x.append(q)
#print(x)
#x=np.sin(2*np.pi*30.0*w)
y=np.zeros(500)
for i in range(500):
    W=w[i]
    for n in range((n1-1)):
     y[i]+=x[n]*np.exp(-1*1j*W*n)
    m.append(abs(y[i]))
    p.append(np.angle(y[i]))
#print(y)
#print(m)
#print(p)
plt.subplot(411)
plt.plot(x)
plt.subplot(412)
plt.plot(y)
plt.subplot(413)
plt.plot(m)
plt.subplot(414)
plt.plot(p)
plt.show()

