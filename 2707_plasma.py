import numpy as np
import matplotlib.pyplot as plt

eps = 10**-4

for G in [0.3, 0.5, 0.8, 1.1, 1.5, 2.0]:
    for i in range(1, 70):
        data = np.loadtxt("C:/Users/Home/Desktop/plasma/Z=1 G = {}/b1.txt".format(G))
        cur_data = np.loadtxt("C:/Users/Home/Desktop/plasma/Z=1 G = {}/b{}.txt".format(G,i))
        data = np.concatenate((data, cur_data), axis=0)

    data = data[abs(data[:, 3] + 1) > eps ]

   """ counts, bins, bars = plt.hist(data[:, 4], bins=90, label='G = {}'.format(G))

    plt.yscale("log")
    plt.ylabel('log g', fontsize='17')
    plt.xlabel('E', fontsize='17')
    plt.title('Z = 1')
    plt.legend()"""
plt.show()