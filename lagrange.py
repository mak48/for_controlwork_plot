import matplotlib.pyplot as plt
import numpy as np

X = [-2,0,1,2]
Y = [3,18,10,3]
Xl = np.linspace(-3,3,100)
Yl = [(17/12*x**3-15/4*x*x-17/3*x+18) for x in Xl]
plt.scatter(X, Y, color='red', label='data')
plt.plot(Xl,Yl, label='Lagrange')
plt.grid()
plt.legend()
plt.show()