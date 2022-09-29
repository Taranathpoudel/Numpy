from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)
count=0
for i in x:
    if i==7:
        count=count+1
print(count)