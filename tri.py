import numpy as np
import matplotlib.pyplot as plt
m=31
t=np.arange(0,m,1)
p=[]
for n in range(0,m):
	w=np.abs(n-((m-1)/2.0))
	y=(2.0*w)/(m-1)
	z=1.0-y
	p=np.append(p,z)

plt.stem(t,p)
plt.show()

