import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--num")

args = parser.parse_args()
num = args.num

data = np.loadtxt("C:/Users/Home/Desktop/plasma/bs1c10-2t.dat")
np.savetxt("C:/Users/Home/Desktop/plasma/b{}.txt".format(num), data)

