import numpy as np
from matplotlib import pyplot as plt

# Create a NumPy array
x=np.arange(1,131)
y1=np.linspace(10,120,90)
y2=np.random.rand(40)
y2=y2*20+ 110
print(x)
print(y1)
print(y2)
y=np.concatenate((y1,y2))
data = np.stack((x,y))
data=np.transpose(data)

# Save the array to a CSV file
np.savetxt('data(1x1,scalar).csv', data, delimiter=',')
plt.plot(x,y)
plt.show()