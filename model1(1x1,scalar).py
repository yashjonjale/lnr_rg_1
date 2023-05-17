import numpy as np
from matplotlib import pyplot as plt

data = np.genfromtxt('data(1x1,scalar).csv', delimiter=',', dtype=float)
print(data)
X=data[:,0]
Y=data[:,1]

X2=np.ones(130,dtype=float)
X3=np.stack((X,X2))
print(X3)
A=X3.T
print(A)
x=np.linalg.inv(np.matmul(A.T,A))
x=np.matmul(x,A.T)
x=np.matmul(x,Y)
print(x)
p=np.array([0,130])
q=np.array([x[1],x[0]*130+x[1]])

plt.plot(p,q,X,Y)
plt.show()

