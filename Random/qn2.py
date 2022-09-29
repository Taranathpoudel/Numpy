# Example
# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

# The probability for the value to be 3 is set to be 0.1

# The probability for the value to be 5 is set to be 0.3

# The probability for the value to be 7 is set to be 0.6

# The probability for the value to be 9 is set to be 0

from numpy import random

# Given array
arr=[3,5,7,9]

# Generating new array
arr1=random.choice(arr,p=[0.1,0.3,0.6,0.0],size=(100))

# Output
print(arr1)
