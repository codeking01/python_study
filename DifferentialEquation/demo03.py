import numpy as np
import matplotlib.pyplot as plt


def simulate_diffusion(init_data, Lz, Nz, T, dt, D):
    dz = Lz / (Nz - 1)
    z = np.linspace(0, Lz, Nz)
    u = np.zeros(Nz)
    u[0] = init_data
    max_iterations = int(T / dt)
    u_time = []
    for iteration in range(max_iterations):
        u_new = u.copy()
        # for i in range(1, Nz - 1):
        #     u_new[i] = u[i] + D * dt / dz ** 2 * (u[i + 1] + u[i - 1]- 2 * u[i])
        # 这一步优化很关键，直接将时间复杂度降低为o(n)
        u_new[1:-1] = u[1:-1] + D * dt / dz ** 2 * (u[2:] + u[:-2] - 2 * u[1:-1])
        if iteration % 100 == 0:
            print(f"iteration:{iteration}")
            u_time.append(u_new.copy())
        u = u_new
    return np.array(u_time)


def plot_heatmap(u_array, T, Lz, num_ticks=6):
    T = T / 3600
    plt.figure(figsize=(10, 6))
    vmin = np.min(u_array)
    vmax = np.max(u_array)
    heatmap = plt.imshow(u_array.T, origin='lower', aspect='auto', extent=[0, T, 0, Lz], cmap='hot',
                         vmin=vmin, vmax=vmax)
    cbar = plt.colorbar(heatmap, label='Concentration')
    ticks = np.linspace(vmin, vmax, num_ticks)
    cbar.set_ticks(ticks)
    tick_labels = ["{:.2f}".format(tick) for tick in ticks]
    cbar.set_ticklabels(tick_labels)
    plt.xlabel('Time (h)')
    plt.ylabel('Concentration')
    plt.title('Concentration Distribution over Time (Heatmap)')
    plt.show()


def plot_easy_heatmap(u_array, T, Lz):
    # 绘制浓度分布热图
    plt.figure(figsize=(10, 6))
    plt.imshow(u_array.T, origin='lower', aspect='auto', extent=[0, T, 0, Lz], cmap='hot')
    plt.colorbar(label='Concentration')
    plt.xlabel('Time (s)')
    plt.ylabel('Concentration')
    plt.title('Concentration Distribution over Time (Heatmap)')
    plt.show()


def plot_concentration_over_time(u_array, z, dt):
    plt.figure(figsize=(10, 6))
    for i, u_t in enumerate(u_array):
        plt.plot(z, u_t, label=f"t = {i * 100 * dt} s")
    plt.xlabel('Time (s)')
    plt.ylabel('Concentration')
    plt.title('Concentration Distribution over Time')
    plt.legend(loc="upper right")
    plt.show()


if __name__ == '__main__':
    # 测试用例
    init_data = 1.0
    Lz = 6.0
    Nz = 500
    T = 200 * 3600
    dt = 0.1
    D = 2.1 * 10 ** (-5)
    u_array = simulate_diffusion(init_data, Lz, Nz, T, dt, D)
    plot_heatmap(u_array, T, Lz)
