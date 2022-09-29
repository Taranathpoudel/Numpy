# Generate 2d array taking random elements from 1d array
# Make 3 rows and 2 column
# given arr=[2,3,5,6,7,8,9]
from numpy import random
arr=[2,3,5,6,7,8,9]
ans=random.choice(arr,size=(3,2))
print(ans)