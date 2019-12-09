import numpy as np
import pandas as pd
df = pd.read_csv(r"C:\Users\Adnan\Dropbox\Documents\Projects\AdventOfCode\AdventOfCode2019\input8.txt", header=None)
coded_image = df.values[0][0]
width = 25
height = 6
num_layers = int(len(coded_image) / (height*width))

layers = []
current_layer = []
pixel_iter = 0
for l in range(num_layers):
    current_layer = []
    for h in range(height):
        current_row = []
        for w in range(width):
            current_row.append(int(coded_image[pixel_iter]))
            pixel_iter += 1
        current_layer.append(current_row)
    layers.append([current_layer])

num_zeros = np.inf
layer_lowest_numbers = None
for layer in layers:
    cur_num_zeros = 0
    for y in layer:
        for x in y:
            cur_num_zeros += sum([1 for p in x if p==0])
    if cur_num_zeros < num_zeros:
        num_zeros = cur_num_zeros
        layer_lowest_numbers = layer
        
num_ones = 0
num_twos = 0
for y in layer_lowest_numbers:
    for x in y:
        num_ones += sum([1 for p in x if p==1])
        num_twos += sum([1 for p in x if p==2])

print('Number of ones multiplied by number of twos: ', num_ones*num_twos)
        
transparent_row = ['2']*width
decoded_image = []
for h in range(height):
    decoded_image.append(transparent_row.copy())

for layer in layers:
    for h in range(height):
        for w in range(width):
            if decoded_image[h][w] == '2':
                if str(layer[0][h][w]) == '0':
                    decoded_image[h][w] = ' '
                else:
                    decoded_image[h][w] = str(layer[0][h][w])

for row in decoded_image:
    print(row)
