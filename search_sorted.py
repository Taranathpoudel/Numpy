# for searching a specefic value in array searchsorted is used
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
id=np.searchsorted(arr,7,side="right") # retutns the index number
print(id)

# Relative search
# the value index can be relative to left to right or right to left
# default it is left to right
# left to right is right
# right to left is left


arr2 = np.array([3,4,5,6,7,8,9])

x = np.searchsorted(arr2, 7, side='left')

print(x)
