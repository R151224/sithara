import matplotlib.pyplot as plt
import numpy as np
fs=input('enter sampling frequency')
f=input('enter the frequency of signal')
t=np.arange(0,10,0.1)
sin1=np.sin(2*np.pi*f*t/fs)
b=np.sin(2*np.pi*f*t/fs)
sin2=2*b
plt.plot(t,sin1)
plt.plot(t,sin2)
plt.show()