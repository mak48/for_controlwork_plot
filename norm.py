from scipy.integrate import quad
def f(x):
    return -2*x**3 + 2*x**2 - 5*x - 5
def g(x, a, b, c):
    return a*x**2 + b*x + c
def error(coeffs):
    a, b, c = coeffs
    error, _ = quad(lambda x: abs(f(x) - g(x, a, b, c)), 0, 5)
    return error
from scipy.optimize import minimize
initial_guess = [0, 0, 0]
result = minimize(error, initial_guess)
print(result.x)