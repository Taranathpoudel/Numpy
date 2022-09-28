import numpy as np
# Use where() with numpy to get the element searched
# It returns the index number of the element of the array
a=np.array([1,2,3,2,5,2,7,2,2])
x=np.where(a==2)
print(x)
for i in x:
    print(a[i])

