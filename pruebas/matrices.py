import numpy as np

#Para los ranges si hay que usar sino t lo multiplica a la lista
#range(3)*2
#np.multiply(range(3),2)

A=np.array([[1,2,3],[4,5,6],[4,5,6]])
acuiS=300.0

At=0.18
tetha=0.5
n=3
l=6
h=np.ones((n,1),float)*10
S=np.identity(n,float)*4
#print S
E=A*tetha-S/(At)
print E
print E*h



h=[2,3,4,5,6]
#h[1:n:l-n+1]
#print h[0:l-n+1:n]

#print range(0,l-n+1,n)
#print range(l-n,l)

#a(3:2:21,:)
#a[ 2:21:2,:]
#every other row of a, starting with the third and going to the twenty-first 
#[1,n:n:l]
for i in np.concatenate(([0],range(n-1,l,n))):
    print i
#print range((1,n),l,n)

print np.linalg.inv(S)
print np.power(S,-1)

