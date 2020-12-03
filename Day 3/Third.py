# read in all data
# with open("Day 3/Testdata.txt",'r') as file:
with open("Day 3/Indata.txt",'r') as file:
    rawData = file.read()

rawDataLines = rawData.splitlines()
length = len(rawDataLines[0])

# Go down the hill
position = 0
treeCollisions = 0
for line in rawDataLines:
    if line[position] == '#':
        treeCollisions += 1
    position += 3
    if position >= length:
        position %= length

print(treeCollisions)
