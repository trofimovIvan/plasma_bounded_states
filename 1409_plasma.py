import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
eps = 10**-4

"TODO: Сделать усреднение для каждой гаммы отдельно. Просчитать среднее время жизни!!" "UPD DONE"
T = 30000  # температура плазмы в К
k = 1.38 * 10 ** (-16)
kT = k * T
e = 4.8 * 10 ** -10
e2 = e ** 2

def mean_live(data):
    data = data[abs(data[:, 3] + 1) > eps]
    times = data[:, -2]*1000
    return np.mean(times)

def G_real_f(Z, G, phi):
    G_real_list = []
    for j in range(1, 16):
        data = np.loadtxt("C:/Users/Home/Desktop/plasma/Z={} G = {} phi={}/b{}.txt".format(Z, G, phi, j)) #подгружаю данные
        "просчитать число электронов, которые живы к данному моменту времени!"
        av_time_live = mean_live(data)
        max_time = data[-1][0]
        moment_list = np.arange(0, max_time + int(av_time_live), int(av_time_live)) # массив времен
        "будем итерироваться по data и смотреть, распалась ли пара за время меньше чем текущее"
        bounden_nums = []
        for k  in range(1, len(moment_list)):
            cur_arr = data[data[:, 0] < moment_list[k]] # массив нужных кентов
            cur_arr = cur_arr[cur_arr[:, 0] >= moment_list[k-1]]
            "среди них теперь найдем тех, кто не распался за этот промежуток."
            "Для этого уберем отсюда всех тех, кто встретился два раза."
            cur_arr = cur_arr[abs(cur_arr[:, 3] + 1) > eps]
            "время жизни при этом равны предпоследнему столбцу. Момент распада при этом равен сумме" \
            " первого столбца и предпоследнего*1000. Получим таким образом список моментов распада пар."
            begin_live = cur_arr[:, 0].reshape(-1, 1)
            end_live = (cur_arr[:, 0] + 1000*cur_arr[:, -2]).reshape(-1, 1)
            lives_arr = np.concatenate((begin_live, end_live), axis=1)

            not_fallen_arr = lives_arr[lives_arr[:, 1] > moment_list[k]]
            bounden_nums.append(len(not_fallen_arr))
        mean_bound = np.mean(bounden_nums)
        "оцениваем гамму"
        alpha = (Z * 100 - mean_bound) / (Z * 100)
        G_real_cur = G * alpha ** (1 / 3)
        G_real_list.append(G_real_cur)
    G_real = np.mean(G_real_list)
    return G_real


def getbins(Z, G, phi, bins=45):
    data = np.loadtxt("C:/Users/Home/Desktop/plasma/Z={} G = {} phi={}/b1.txt".format(Z, G, phi))

    for i in range(2, 16):
        cur_data = np.loadtxt("C:/Users/Home/Desktop/plasma/Z={} G = {} phi={}/b{}.txt".format(Z, G, phi, i))
        data = np.concatenate((data, cur_data), axis=0)

    data = data[abs(data[:, 3] + 1) > eps]

    counts, bins, bars = plt.hist(data[:, 4], bins=bins, density=True, alpha=0)

    bins = bins[1:]
    return bins[-1]

G_real_a = []
delta_E_a = []
for phi in ['2pi']:
    G_real = []
    delta_E = []
    for G in [0.3, 0.5, 0.8, 1.1, 2.0]:
        G_real.append(G_real_f(Z=2, G=G, phi=phi))
        delta_E.append(abs(getbins(Z=2, G=G, phi=phi)))
    G_real_a.append(G_real)
    delta_E_a.append(delta_E)
plt.show()

lr1 = LinearRegression()
lr2 = LinearRegression()
lr3 = LinearRegression()
G_real_a[0] = np.array(G_real_a[0]).reshape(-1, 1)
"""G_real_a[1] = np.array(G_real_a[1]).reshape(-1, 1)
G_real_a[2] = np.array(G_real_a[2]).reshape(-1, 1)"""
delta_E_a[0] = np.array(delta_E_a[0]).reshape(-1, 1)
"""delta_E_a[1] = np.array(delta_E_a[1]).reshape(-1, 1)
delta_E_a[2] = np.array(delta_E_a[2]).reshape(-1, 1)"""
lr1.fit(G_real_a[0], delta_E_a[0])
"""lr2.fit(G_real_a[1], delta_E_a[1])
lr3.fit(G_real_a[2], delta_E_a[2])"""

plt.plot(G_real_a[0], delta_E_a[0], 'ro', label='2pi')
"""plt.plot(G_real_a[1], delta_E_a[1], 'bo', label='4pi')
plt.plot(G_real_a[2], delta_E_a[2], 'go', label='6pi')"""
plt.plot(G_real_a[0], lr1.predict(G_real_a[0]), color='red')
"""plt.plot(G_real_a[1], lr2.predict(G_real_a[1]), color='blue')
plt.plot(G_real_a[2], lr3.predict(G_real_a[2]), color='green')"""
plt.legend(fontsize='12')
plt.xlabel(r'$\Gamma$', fontsize='17')
plt.ylabel(r'$\Delta E$', fontsize='17')
plt.show()