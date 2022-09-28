import numpy as np
# Use array_split() function to split the array
# arguments 1.array name 2.spliting_part
# Make sure the length of array is divisible by splitting_part
a=np.array([1,2,3,4,5,6])
c=np.array_split(a,3)
print(c)

# Accessig the splited arrays
# Arrays can be accessed by using array index number
print(c[0])
print(c[1])
print(c[2])