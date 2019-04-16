def conv(a,b):
	n1=len(x1)
	n2=len(h1)
	x=[]
	h=[]
	p=0
	if(n1>n2):
		for i in range(0,n1-n2):
			h1.append(p)
		#print(h1)
	else:
		for t in range(0,n2-n1):
			x1.append(p)
		#print(x1)
	x=x1
	h=h1
	print(x)
	print(h)
	z=len(x)+len(h)-1
	con=[]
	for n in range(0,z,1):	
		sum=0
		for k in range(0,n1,1):
			if((n-k)>=0 and (n-k)<n1):
				sum = sum + ((x[k])*(h[n-k]))
		con.append(sum)	
	print(con)
x1=input("Enter x1:")# like x1=[1,2,3]
h1=input("Enter h1:")# like y1=[1,2,3]
conv(x1,h1)
