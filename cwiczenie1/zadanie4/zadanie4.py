import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
from mat4py import loadmat

data01=loadmat('Data01.mat')
print(np.transpose(data01['t'])[0,1])
plt.plot(np.transpose(data01['t'])[0],np.transpose(data01['y'])[0], '.r')
plt.xlabel('t')
plt.ylabel('y')
plt.show()
