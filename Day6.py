import numpy as np
import pandas as pd
df = pd.read_csv(r"C:\Users\Adnan\Dropbox\Documents\Projects\AdventOfCode\2019\input6.txt", header=None, sep = ")")
orbited = df[0]
orbiter = df[1]

orbits = pd.Series(orbited.values, orbiter.values).to_dict()
num_orbits = 0
orbiter = list(orbits.keys())

for orbit in orbiter:
    next_orbit = orbit
    while next_orbit != 'COM':
        num_orbits += 1
        next_orbit = orbits[next_orbit]

print('Number of orbits: ', num_orbits)

orbit_start = 'YOU'
orbit_end = 'SAN'
shortest_path = np.inf

you_to_com = []
san_to_com = []

next_orbit = 'YOU'
while next_orbit != 'COM':
    you_to_com.append(next_orbit)
    next_orbit = orbits[next_orbit]
next_orbit = 'SAN'
while next_orbit != 'COM':
    san_to_com.append(next_orbit)
    next_orbit = orbits[next_orbit]
    
[you_to_com.append(x) for x in san_to_com]

you_to_san = [x for x in you_to_com if you_to_com.count(x) == 1]

print('Orbital transfers to reach Santa: ', len(you_to_san)-2)


