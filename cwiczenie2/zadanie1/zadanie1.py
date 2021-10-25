from mat4py import loadmat
import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp
from cvxpy.atoms.sigma_max import sigma_max as norm2
from cvxpy.atoms.norm1 import norm1
# from numpy.linalg import norm


data01 = loadmat('../Data01.mat')
t = np.array(data01['t'])
y = np.array(data01['y'])
n=t.size*1
q=2

v=cp.Variable((n,1))
D=np.eye(n-1)
D1=np.hstack([-D,np.zeros([n-1,1])])
D2=np.hstack([np.zeros([n-1,1]),D])
D=D1+D2
objective = cp.Minimize(norm2(y-v)*1)
constraints=[
    norm1(D@v)<=q
]
p1 = cp.Problem(objective, constraints)
p1.solve(verbose=True)
print(v.value)
# plotting
plt.plot(t,y, 's', color='gray', markersize=3)
plt.xlabel('t')
plt.ylim([-0.2,1.2])
plt.grid('minor')
plt.show()
