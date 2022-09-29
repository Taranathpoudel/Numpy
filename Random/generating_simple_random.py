from numpy import random

# Generating random integer
x=random.randint(100)
print(x)

# Generating random flot
y=random.rand()
print(y)

# Generating random array
arr=random.randint(100,size=(5))
print(arr)

# Generate 2-D random array
arr2=random.randint(100,size=(2,3))
print(arr2)

# Generating random number from an array
# This can be done using choice function
chs=random.choice(arr)
print(chs)

# chooses a random number from arr=[]


