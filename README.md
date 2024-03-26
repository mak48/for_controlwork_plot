## 5 номер
### *Построенный график*

![image](https://github.com/mak48/for_controlwork_plot_lagrange/assets/132274048/8b2b5602-a629-4687-a3ce-795d8603c64c)

### *Код*
```
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
```

## 6 номер
### *Построенные кривые безье*

![image](https://github.com/mak48/for_controlwork_plot/assets/132274048/abdf90cd-e400-4b06-864c-b4b29613af18)

### *Код*
```
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
```
