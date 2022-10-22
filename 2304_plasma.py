import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

eps = 10**-4

"""data = np.loadtxt("C:/Users/Home/Desktop/plasma/bs1c10-2t.dat")
np.savetxt("C:/Users/Home/Desktop/plasma/b10.txt", data)"""

def getbins(Z, G, phi, bins=45):
    data = np.loadtxt("C:/Users/Home/Desktop/plasma/Z={} G = {} phi={}/b1.txt".format(Z, G, phi))


    for i in range(2, 30):
        cur_data = np.loadtxt("C:/Users/Home/Desktop/plasma/Z={} G = {} phi={}/b{}.txt".format(Z, G, phi, i))
        data = np.concatenate((data, cur_data), axis=0)

    data = data[abs(data[:, 3] + 1) > eps]

    counts, bins, bars = plt.hist(data[:, 4], bins=bins, density=True)
    bins = bins[1:]
    plt.errorbar(bins, counts, fmt='s')


    plt.yscale("log")
    plt.ylabel('log g', fontsize='17')
    plt.xlabel('E', fontsize='17')
    plt.title('Z = {}, G = {}'.format(Z, G))
    print(bins[-1])


getbins(Z=2, G=0.3, phi="8pi")

data = np.loadtxt("C:/Users/Home/Desktop/plasma/b1.txt")


for i in range(2, 14):
    cur_data = np.loadtxt("C:/Users/Home/Desktop/plasma/b{}.txt".format(i))
    data = np.concatenate((data, cur_data), axis=0)

data = data[abs(data[:, 3] + 1) > eps ]


counts, bins, bars = plt.hist(data[:, 4], bins=45, density=True)
bins = bins[1:]
plt.errorbar(bins, counts, fmt='s')
print(bins[-1])

plt.yscale("log")
plt.ylabel('log g', fontsize='17')
plt.xlabel('E', fontsize='17')


plt.show()