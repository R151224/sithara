import numpy as np
import cmath as c
import matplotlib.pyplot as plt
w=np.linspace(-4*np.pi,4*np.pi,1000)
s=c.sqrt(-1)
a=input('enter no of elements')
x=np.zeros(a)
z=[]
h=[]
for i in range(a):
  x[i]=input('enter values')
print x
y=np.zeros(1000)
for j in range(1000):
     W=w[j]
     for k in range(a):
      y[j]+=x[k]*np.exp(-s*W*k)
     z.append(abs(y[j]))
     h.append(np.angle(y[j]))
print y
plt.subplot(311)
plt.plot(w,y)
plt.subplot(312)
plt.plot(w,z)
plt.subplot(313)
plt.plot(w,h)
plt.show()


  
