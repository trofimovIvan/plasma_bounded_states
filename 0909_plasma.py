import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--phi")
parser.add_argument("--G")

args = parser.parse_args()
phi = args.phi
G = args.G

par_file = open("C:/Users/Home/Desktop/plasma/par.dat", 'r')
par_lines = par_file.readlines()
par_file.close()
index1 = par_lines.index("MaxPhase = {}  ; in units of 2pi\n".format(phi-2))
par_lines[index1] = "MaxPhase = {}  ; in units of 2pi".format(phi)
index2 = par_lines.index("Gamma_ee  =    ; 0.63972 1.27944 2.55888 5.11776\n")
par_file = open("C:/Users/Home/Desktop/plasma/par.dat", "w")
for str in par_lines:
    print(str, file=par_file, end="")