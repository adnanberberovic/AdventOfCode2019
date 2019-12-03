import numpy as np
import pandas as pd
import re
df = pd.read_csv(r"H:\AdventOfCode\input3.txt", header=None, sep=",")
paths = df.transpose()
pathsList = []
for i in range(paths.shape[1]):
    pathsList.append(paths[i])

grids = []
nextPosition = (0,0)
wireCounter = 0
for wire in pathsList:
    gc = 0
    grid = []
    grid.append((0,0))
    for i in range(len(wire)):
        if isinstance(wire[i], str):
            direction = wire[i][0]
            step = int(wire[i][1:])
            for j in range(step):
                gc += 1
                nextPosition = grid[gc-1]
                if direction == 'R':
                    nextPosition = (nextPosition[0]+1, nextPosition[1])
                elif direction == 'U':
                    nextPosition = (nextPosition[0], nextPosition[1]+1)
                elif direction == 'L':
                    nextPosition = (nextPosition[0]-1, nextPosition[1])
                elif direction == 'D':
                    nextPosition = (nextPosition[0], nextPosition[1]-1)
                grid.append(nextPosition)
        else:
            break
    grids.append(grid)
    wireCounter += 1

intersections = []
dfg1 = pd.DataFrame(grids[0], columns = ['Xpos', 'Ypos'])
dfg2 = pd.DataFrame(grids[1], columns = ['Xpos', 'Ypos'])
intersections = pd.merge(dfg1, dfg2, how='inner', left_on=['Xpos', 'Ypos'], right_on=['Xpos', 'Ypos'])
shortestDistance = np.inf
for intersection in intersections.iterrows():
    if (abs(intersection[1]['Xpos']) + abs(intersection[1]['Ypos']) < shortestDistance) and not(abs(intersection[1]['Xpos']) == 0 and abs(intersection[1]['Ypos']) == 0):
        shortestDistance = abs(intersection[1]['Xpos']) + abs(intersection[1]['Ypos'])

stepsToIntersection1 = []
stepsToIntersection2 = []
stepsTotal = []
for intersection in intersections.iterrows():
    if not(abs(intersection[1]['Xpos']) == 0 and abs(intersection[1]['Ypos']) == 0):
        dfg1x = dfg1.loc[dfg1['Xpos'] == intersection[1]['Xpos']]
        dfg1y = dfg1x.loc[dfg1x['Ypos'] == intersection[1]['Ypos']]
        stepsToIntersection1.append(dfg1y.index[0])
        dfg2x = dfg2.loc[dfg2['Xpos'] == intersection[1]['Xpos']]
        dfg2y = dfg2x.loc[dfg2x['Ypos'] == intersection[1]['Ypos']]
        stepsToIntersection2.append(dfg2y.index[0])
        stepsTotal.append(dfg1y.index[0] + dfg2y.index[0])



print("Manhattan distance: ", shortestDistance)
print("Minimum steps: ", min(stepsTotal))
print('eoc')