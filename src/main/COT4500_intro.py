import numpy as np

array = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

for x in range(0, 3):
    for y in range(0, 3):
        if x == y:
            array[x][y] = 1
        else:
            array[x][y] = 0
print(array, end="\n\n")
for x in range(0, 3):
    for y in range(0, 3):
        if x != y:
            array[x][y] = 3
print(array, end="\n\n")
array = np.delete(array, 2, 1)
print(array)
