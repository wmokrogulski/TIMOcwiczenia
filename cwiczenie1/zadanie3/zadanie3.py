import cvxpy as cp
import numpy as np

x_sur1 = cp.Variable()
x_sur2 = cp.Variable()
x_lek1 = cp.Variable()
x_lek2 = cp.Variable()

costs = 100.0 * x_sur1 + 199.9 * x_sur2 + 700.0 * x_lek1 + 800.0 * x_lek2
income = 6500 * x_lek1 + 7100 * x_lek2

objective = cp.Minimize(costs - income)

# bilans czynnika aktywnego
active_element_constraint = [0.01 * x_sur1 + 0.02 * x_sur2 - 0.5 * x_lek1 - 0.6 * x_lek2 >= 0]
# warehouse
warehouse_constraint = [x_sur1 + x_sur2 <= 1000]
# human resources
hr_constraint = [90 * x_lek1 + 100 * x_lek2 <= 2000]
# hardware resources
hardware_constraint = [40 * x_lek1 + 50 * x_lek2 <= 800]
# budget
budget_constraint = [100 * x_sur1 + 199.9 * x_sur2 + 700 * x_lek1 + 800 * x_lek2 <= 100000]
# minimal quantities
minimal_constraint = [
    x_sur1 >= 0,
    x_sur2 >= 0,
    x_lek1 >= 0,
    x_lek2 >= 0
]

constraints = []
constraints.extend(active_element_constraint)
constraints.extend(warehouse_constraint)
constraints.extend(hr_constraint)
constraints.extend(hardware_constraint)
constraints.extend(budget_constraint)
constraints.extend(minimal_constraint)

p1 = cp.Problem(objective, constraints)
p1.solve()

# output
print(f'ilość surowca 1: {x_sur1.value:.3f}')
print(f'ilość surowca 2: {x_sur2.value:.3f}')
print(f'ilość leku 1: {x_lek1.value:.3f}')
print(f'ilość leku 2: {x_lek2.value:.3f}')
