import numpy as np
from scipy.integrate import quad
def f(x):
    return np.sqrt(x+6)
def error(coeffs):
    h = np.poly1d(coeffs)
    error, _ = quad(lambda x: (h(x)**2) / np.sqrt((1 - (2*x - 7)**2) / 9), 2, 5)
    return error
from scipy.optimize import minimize
initial_guess = [f(x) for x in [2,3,4,5]]
result = minimize(error, initial_guess)
print(result.x)