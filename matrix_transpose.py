r=input("enter the rows")
c=input("enter the columns")
i=0
a={}
b={}
while(i<r):
           j=0
	   while(j<c):
		m1=input("enter matrix elements")
                b[j,i]=m1
		a[i,j]=m1
		j=j+1
	   i=i+1
i=0
while(i<r):
     j=0
     while(j<c):
         print a[i,j]
         j=j+1
     i=i+1
j=0
while(j<r):
        i=0
        while(i<c):
               print b[j,i]
               i=i+1
        j=j+1

