
from arithmatic import addition,subtraction
import math
import random

addition(10,20)
subtraction(100,50)

print("squar root of 16:",math.sqrt(16))
print("3 power of 2:",math.pow(2,3))
print("89.98:",math.floor(89.98))
print("89.98:",math.ceil(89.98))

# Choosing a random element from a list
colors = ["Red", "Blue", "Green", "Yellow"]
print("Random color:", random.choice(colors))

print(colors)

random.shuffle(colors)
print("Shuffled list:", colors)

print("Random number between 1 and 10:", random.randint(1, 10))