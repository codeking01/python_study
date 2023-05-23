# author: code_king
# time: 2023/5/16 22:55
# file: demo02.py
import numpy as np
import matplotlib.pyplot as plt

Lx = 6.0  # x方向区域长度
Ly = 6.0  # y方向区域长度
Nx = 20  # x方向网格数
Ny = 20  # y方向网格数
# Nx = 6000  # x方向网格数
# Ny = 6000  # y方向网格数
T = 25000 # 总时间
dt = 0.1  # 时间步长
# 扩散系数
D = 5*10**(-5)
# 系数
R=10**(-7)

dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)

# 创建浓度分布数组
u = np.zeros((Nx, Ny))

# 设置初始条件
u[int(Nx/2), int(Ny/2)] =0.04 /3600  # 在中心设置初始浓度

# 迭代求解
max_iterations = int(T / dt)
for iteration in range(max_iterations):
    u_new = u.copy()
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            u_new[i, j] = u[i, j] + D * dt / dx**2 * (u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1] - 4 * u[i, j])+dt*R
    # print(f"iteration:{iteration}")
    u = u_new

# 绘制结果
X, Y = np.meshgrid(x, y)
plt.figure()
plt.contourf(X, Y, u.T, cmap='hot')
plt.colorbar(label='Concentration')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Diffusion Equation Solution')
plt.show()
print("结束！")