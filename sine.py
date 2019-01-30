import numpy as np
import matplotlib.pyplot as mp
t=np.arange(0,10,0.1)
x1=np.sin(2*np.pi*t)
mp.plot(t,x1)
mp.xlabel('time')
mp.ylabel('amplitude')
mp.show()