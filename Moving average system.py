import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
p=input("enter order of the moving average system:")
fs=1000
#sample=100
f=10
f2=300
x=np.linspace(0,400,200)
#x=np.arange(sample)
output=np.zeros(200)
y1=np.sin(2 * np.pi * f * x/fs)
y2=np.sin(2 * np.pi * f2 * x/fs)
#y2=np.random.rand(sample) 
y=y1+y2
#sum=0
for i in range(0,200,1):
	for k in range(0,p-1,1):
		sum += y[i-k]
	print sum
	output[i]=float((sum)/(p))
	#sum=0
print output
plt.subplot(4,1,1)
plt.plot(x,y1,'k')
plt.subplot(4,1,2)
plt.plot(x,y2,'b')
plt.subplot(4,1,3)
plt.plot(x,y,'g')
plt.subplot(4,1,4)
plt.plot(x,output,'k')
plt.show()
