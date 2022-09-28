# create an array of even & odd numbers from the given array
arr=[1,2,3,4,5,6,7,8,9]
import numpy as np
arr1=np.copy(arr)
ev=np.where(arr1%2==0)
for i in ev:
    print(arr1[i])

od=np.where(arr1%2==1)
for j in od:
    print(arr1[j])