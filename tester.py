# library
import random
import numpy as np

# establish min, max, mean, sd height
minHeight = 68; maxHeight = 90; meanHeight = 79; sdHeight = 3
        
        # generate height
height = np.random.normal(meanHeight, sdHeight)
        
        # correct outliers
if height < minHeight: height = minHeight
elif height > maxHeight: height = maxHeight

# round value
height = round(height)

        
# establish weight ranges
weightRange = {
    (68, 72): {'minWeight': 150, 'maxWeight': 180, 'meanWeight': 165, 'sdWeight': 5},
    (73, 78): {'minWeight': 180, 'maxWeight': 220, 'meanWeight': 200, 'sdWeight': 10},
    (79, 84): {'minWeight': 220, 'maxWeight': 260, 'meanWeight': 240, 'sdWeight': 10},
    (85, 90): {'minWeight': 260, 'maxWeight': 300, 'meanWeight': 280, 'sdWeight': 10}
}
        
# gather weight parameters
for range, params in weightRange.items():
    if range[0] <= height <= range[1]:
        minWeight = params['minWeight']
        maxWeight = params['maxWeight']
        meanWeight = params['meanWeight']
        sdWeight = params['sdWeight']
        break
        
# generate weight
weight = np.random.normal(meanWeight, sdWeight)
        
# correct outliers
if weight < minWeight: weight = minWeight
elif weight > maxWeight: weight = maxWeight

# round value
weight = round(weight)

print(height, weight)

# convert height
feet = height // 12
inches = height % 12

print('feet ', feet, ' inches ', inches)