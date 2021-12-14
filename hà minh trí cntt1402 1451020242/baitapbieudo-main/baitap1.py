import matplotlib.pyplot as plt
import numpy.random as rd
x = rd.normal(5,1,1000)
y = rd.normal(6,1,1000)

plt.scatter(x,y)
plt.show()