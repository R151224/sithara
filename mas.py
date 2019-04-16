import numpy as np
import matplotlib.pyplot as plt
p=input("enter the order of the moving average system")
fs=4000
f1=10
f2=700
y=np.zeros(200)
#t=np.linspace(0,20,20)
t=np.linspace(0,700,200)
u=np.sin(2*np.pi*f1*t/fs)
v=np.sin(2*np.pi*f2*t/fs)
#x=[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
x=u+v
sum=0
for i in range(0,200,1):
		for k in range(0,p-1,1):
				sum=sum+x[i-k]
		print sum
		y[i]=float((sum)/(p))
		sum=0
print y
plt.subplot(4,1,1)
plt.plot(t,u)
plt.subplot(4,1,2)
plt.plot(t,v)
plt.subplot(4,1,3)
plt.plot(t,x)
plt.subplot(4,1,4)
plt.plot(t,y)
plt.show( )
