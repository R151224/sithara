import numpy as np
import matplotlib. pyplot as plt
import cmath as cm


wp=0.35*np.pi
ws=0.7*np.pi
ds=0.1
dp=0.6
T=0.1
e=np.sqrt((1/dp**2)-1)
print e
b=((1/e**2)+1)

def analog(wp,ws):
      Ap=((2/T)*np.tan(wp/2))
      As=((2/T)*np.tan(ws/2))
      return Ap,As

A=analog(wp,ws)
Ap=A[0]
print Ap
As=A[1]
print As



#order
def order(ds,dp,As,Ap):
       x1=((1.0/(ds**2))-1.0)
       x2=((1.0/(dp**2))-1.0)
       x=(x1/x2)
       y=(np.arccosh(cm.sqrt(x))/np.arccosh(As/Ap))
       return y

N=order(ds,dp,As,Ap)
n1=abs(N)
n2=np.ceil(n1)
print "order=", n2

#cutoff frequency

#def    cutoff(As,ds,n2):
 #        t1=(1.0/(2.0*n2))
     #    t2=((1.0/ds**2)-1)
      #   t3=t2**t1
       #  y=As/t3
        # return y

#Ac=cutoff(As,ds,n2)
#print "cutoff frequency",Ac


          
#transfer function
y1=((np.sqrt(b)+(1/e))**(1/n2))
y2=((np.sqrt(b)+(1/e))**(-1/n2))
yn=0.5*(y1-y2)
print 'yn=',yn
k=(n2/2)
j=cm.sqrt(-1)
x1=(2*k-1)*np.pi
x2=2*n2
bk=2*yn*np.sin(x1/x2)
print 'bk=',bk
c1=np.cos(x1/x2)
ck=(yn**2)+(c1**2)
print 'ck',ck
w=np.arange(0,np.pi,0.01)
z=np.exp(-j*w)
s=(2/T)*((1-z**(-1))/(1+z**(-1)))
h1=(s**2)+(bk*Ap*s)+((Ap**2)*ck)
hs=(1/np.sqrt(1+e**2)*(((Ap)**2)*ck)/h1)
plt.plot(w,abs(hs))
plt.show()
       






	

