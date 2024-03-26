import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.Symbol('t')
x1 = sp.sympify('-11*t**3+19.5*t**2-4.5*t+3.5')
y1 = sp.sympify('0.5*t**3-1.5*t**2+1.5*t+6.5')
x2 = sp.sympify('-5*t**3+4.5*t**2+4.5*t+3.5')
y2 = sp.sympify('-2.5*t**3+4.5*t**2-1.5*t+6.5')
interval1 = np.arange(0, 1, 0.01)
interval2 = np.arange(0, 1, 0.01)
x_values1 = [x1.subs(t, value) for value in interval1]
y_values1 = [y1.subs(t, value) for value in interval1]
x_values2 = [x2.subs(t, value) for value in interval2]
y_values2 = [y2.subs(t, value) for value in interval2]
plt.xlim(1.5, 8.5)
plt.ylim(5.5, 7.5)
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
#данные точки
X = [2,5,8,7,2]
Y = [7,6,7,7,7]
plt.scatter(X, Y, color='black', label='data')
plt.plot(X, Y,color='black')
#середины сторон
X = [3.5,7.5]
Y = [6.5,7]
plt.scatter(X, Y, color='green', label='середины AB и CD')
plt.plot(x_values1, y_values1)
plt.plot(x_values2, y_values2)
plt.grid()
plt.show()