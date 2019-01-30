import matplotlib.pyplot as plt
import numpy as np

Fs=8000
f=5
sample=8000
x=np.arange(sample)
y1=np.sin((2*np.pi*f*x/Fs)+np.pi/2)
y2=np.sin((2*np.pi*f*x/Fs))
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()