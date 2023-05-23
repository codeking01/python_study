# author: code_king
# time: 2023/5/16 10:15
# file: demo01.py
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(t, y):
    return y ** 2


t_start = 0
t_end = 10
y_0 = 1

t = np.linspace(t_start, t_end, 100)
y = odeint(model, y_0, t)

plt.plot(t, y)
plt.show()
