import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
from mat4py import loadmat
from scipy.optimize import linprog

# import danych
data01 = loadmat('Data01.mat')
x = np.array(data01['t'])
y = np.array(data01['y'])
A = np.hstack((x, np.ones(x.shape)))
N=x.shape[0]

# metoda najmniejszych kwadratów
B = np.linalg.pinv(A) @ y
als = B[0, 0]
bls = B[1, 0]
print('ls')
print(f'als={als:.4f}, bls={bls:.4f}')

# metoda programowania liniowego
c = np.vstack((np.zeros((2, 1)), np.ones(y.shape)))
A_ub = np.hstack((np.vstack((A, -A)), np.vstack((-np.eye(N), -np.eye(N)))))
b_ub = np.vstack((y, -y))
print('lp')
alp, blp = linprog(c.T, A_ub, b_ub).x[:2]
print(f'alp={alp:.4f} blp={blp:.4f}')

# plotting
plt.plot(x, y, '.r', label='data')
plt.plot(x, (als*x.T+bls*np.ones(N).T)[0],'k', label='ls')
plt.plot(x, (alp*x.T+blp*np.ones(N).T)[0], label='lp')
plt.xlim([0,10])
plt.ylim([2,10])
plt.legend()
plt.grid('minor')
# plt.plot(x.T, alp*x.T+blp, 'b')
plt.savefig('lines.png')
plt.show()
