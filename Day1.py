import numpy as np
import pandas as pd
df = pd.read_csv(r"H:\AdventOfCode\input1.txt", header=None)
total_fuel_req = 0
for module in df.iterrows():
    weight = module[1][0]
    fuel = np.floor(weight/3) - 2
    fuel_weight = 0
    fuel_weight_add = np.floor(fuel/3) - 2
    while fuel_weight_add > 0:
        fuel_weight += fuel_weight_add
        fuel_weight_add = np.floor(fuel_weight_add/3) - 2
    total_fuel_req += fuel + fuel_weight
print(total_fuel_req)


print('eoc')