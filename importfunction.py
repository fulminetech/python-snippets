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
