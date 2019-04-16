import numpy as np
import matplotlib.pyplot as plt
m=31
t=np.arange(0,m,1)
p=[]
for n in range(0,m):
	w=np.cos((2*np.pi*n)/(m-1))
	y=0.46*w
	z=0.54-y
	p=np.append(p,z)
plt.stem(t,p)
plt.show()
	

