from importfunction import filterLimit
import random

randomlist = []

# Generates a random list of 10 elements
for i in range(0,10):
    n = random.randint(60,100)
    randomlist.append(n)

print(randomlist)
print(filterLimit(randomlist, 70, 90))
