import random
randomlist = []

# Generates list of 5 elemets between 60 and 100
for i in range(0,5):
    n = random.randint(60,100)
    randomlist.append(n)

print(randomlist)