# read in all data
# with open("Day 3/Testdata.txt",'r') as file:
with open("Day 3/Indata.txt",'r') as file:
    rawData = file.read()

rawDataLines = rawData.splitlines()
length = len(rawDataLines[0])

# Go down the hill

def Downhill(slopeList, right, down):
    """
    Method counting the number of trees hit if going down a given slope according to right and down instructions.
    """
    lengthOfSlopeSegment = len(slopeList[0])
    position = 0
    treeCollisions = 0
    slopeIndex = 0
    line = slopeList[slopeIndex]
    while True:
        # Check for tree collision
        if line[position] == '#':
            treeCollisions += 1

        # Update movement to the right
        position += right
        if position >= lengthOfSlopeSegment:
            position %= lengthOfSlopeSegment
        
        # Take next line, or end
        if slopeIndex + down >= len(slopeList):
            break
        else:
            slopeIndex += down
            line = slopeList[slopeIndex]
    return treeCollisions

result1 = Downhill(rawDataLines, 1, 1)
print(result1)
result2 = Downhill(rawDataLines, 3, 1)
print(result2)
result3 = Downhill(rawDataLines, 5, 1)
print(result3)
result4 = Downhill(rawDataLines, 7, 1)
print(result4)
result5 = Downhill(rawDataLines, 1, 2)
print(result5)

print("{} {} {} {} {}".format(result1, result2, result3, result4, result5))
print(result1*result2*result3*result4*result5)

# position = 0
# treeCollisions = 0
# for line in rawDataLines:
#     if line[position] == '#':
#         treeCollisions += 1
#     position += 3
#     if position >= length:
#         position %= length

# print(treeCollisions)
