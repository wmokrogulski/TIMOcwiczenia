import cvxpy as cp
import numpy as np

x1 = cp.Variable()  # ilość pszenicy
x2 = cp.Variable()  # ilość soi
x3 = cp.Variable()  # ilość mączki

objective = cp.Minimize(300 * x1 + 500 * x2 + 800 * x3)

constraints = [
    0.8 * x1 + 0.3 * x2 + 0.1 * x3 >= 0.3,
    0.01 * x1 + 0.4 * x2 + 0.7 * x3 >= 0.7,
    0.15 * x1 + 0.1 * x2 + 0.2 * x3 >= 0.1,
    x1 >= 0,
    x2 >= 0,
    x3 >= 0
]

p1 = cp.Problem(objective, constraints)
p1.solve()

print(f'ilosc przenicy: {x1.value:.4f} t')
print(f'ilosc soi: {x2.value:.4f} t')
print(f'ilosc mączki: {x3.value:.4f} t')
