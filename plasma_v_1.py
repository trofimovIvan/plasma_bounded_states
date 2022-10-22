import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plot import read_file_txt

#names=['Step', 'Ni', 'Ne', '<R>', '<E>', 'duration', 'phase']
def read_file(filename, header):
    with open(filename, 'r') as data_file:
        strings = data_file.readlines()[header:]
        n = len(strings)
        df = pd.DataFrame(columns=strings[0].split())
        for i in range(1, n):
            cur_str = strings[i].split()
            for j in range(len(cur_str)):
                cur_str[j] = float(cur_str[j])
            df.loc[len(df)] = cur_str
    return df

def correct_data(df):
    df1 = df.loc[abs(df['<R>'] + 1) >= 0.001]

    return df1

def plot_hist(data_frame, column_name):
    to_plot = data_frame[column_name]
    plt.hist(to_plot, bins=20, density=True)
    plt.ylabel('Density pair', fontsize='17')
    plt.xlabel('<E>', fontsize='17')
    plt.show()

"""data = read_file('C:/Users/Home/Desktop/plasma/bs1c10-2t.dat', header=53)

cor_data = correct_data(data)
print(cor_data)
plot_hist(cor_data, '<E>')"""


