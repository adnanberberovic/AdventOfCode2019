import numpy as np
import pandas as pd
df = pd.read_csv(r"H:\AdventOfCode\input2.txt", header=None, sep=",")
int_input_base = df.values.tolist()[0]

for i1 in range(100):
    for i2 in range(100):
        int_input = int_input_base.copy()
        int_input[1] = i1
        int_input[2] = i2
        i = 0
        while i <= len(int_input):
            if int_input[i] == 1:
                int_input[int_input[i+3]] = int_input[int_input[i+2]] + int_input[int_input[i+1]]
            if int_input[i] == 2:
                int_input[int_input[i+3]] = int_input[int_input[i+2]] * int_input[int_input[i+1]]
            if int_input[i] == 99:
                break
            i += 4
        if int_input[0] == 19690720:
            print(int_input[1])
            print(int_input[2])
            print(100*int_input[1] + int_input[2])
            break
    if int_input[0] == 19690720:
        break

print('eoc')