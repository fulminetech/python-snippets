import random
randomlist = []
processedlist = []

# Generates a random list of 10 elements
for i in range(0,10):
    n = random.randint(60,100)
    randomlist.append(n)

# Creates a copy if list for further processing
processedlist = randomlist.copy()

upperlimit = 90
lowerlimit = 60

# Values above and below limits are set red and in between are blue
for index, items in enumerate(processedlist):
    if items > upperlimit or items < lowerlimit:
        processedlist[index] = "red"
    elif items >= lowerlimit and items <= upperlimit:
    # elif:
        processedlist[index] = "blue"

print(randomlist)
print(processedlist)

# Useable function to do the above
def filterLimit(processedlist, lowerlimit, upperlimit):
    # Values above and below limits are set red and in between are blue
    for index, items in enumerate(processedlist):
        if items > upperlimit or items < lowerlimit:
            processedlist[index] = "red"
        elif items >= lowerlimit and items <= upperlimit:
        # elif:
            processedlist[index] = "blue"
    return processedlist

print(filterLimit(randomlist, 60, 90))