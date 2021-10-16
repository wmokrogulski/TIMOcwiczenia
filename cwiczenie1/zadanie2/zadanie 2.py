import cvxpy as cp
import numpy as np

x1 = cp.Variable()  # ilość płatków
x2 = cp.Variable()  # ilość mleka
x3 = cp.Variable()  # ilość chleba

objective = cp.Minimize(.15 * x1 + .25 * x2 + .05 * x3)  # koszty

calories_constraints = [
    2250 >= 70 * x1 + 121 * x2 + 65 * x3,
    70 * x1 + 121 * x2 + 65 * x3 >= 2000
]
vitamines_constraints = [
    1e4 >= 107 * x1 + 500 * x2 + 0 * x3,
    107 * x1 + 500 * x2 + 0 * x3 >= 5e3
]
sugar_constraint = [
    45 * x1 + 40 * x2 + 60 * x3 <= 1000
]
quantity_constraints = [
    10 >= x1,
    x1 >= 0,
    10 >= x2,
    x2 >= 0,
    10 >= x3,
    x3 >= 0
]
constraints = []
constraints.extend(calories_constraints)
constraints.extend(vitamines_constraints)
constraints.extend(sugar_constraint)
constraints.extend(quantity_constraints)

p1 = cp.Problem(objective, constraints)
p1.solve()

print(f'ilosc płatków: {x1.value:.4f} porcji')
print(f'ilosc mleka: {x2.value:.4f} porcji')
print(f'ilosc chleba: {x3.value:.4f} porcji')
