# with open("Day 5/Testdata.txt",'r') as file:
with open("Day 5/Indata.txt",'r') as file:
    rawData = file.read()

rawDataLines = rawData.splitlines()

def BinarySplit(input, takeLow):
    """
    A method that takes a list and returns either the lower or higher half of it.
    """
    middle = int(len(input) / 2)
    if takeLow:
        return input[:middle]
    else:
        return input[middle:]

seatIDs = []
for rawDataLine in rawDataLines:
    # Binary search on row
    rows = list(range(128))
    for char in rawDataLine[:7]:
        if char == 'F':
            rows = BinarySplit(rows, True)
        elif char == 'B':
            rows = BinarySplit(rows, False)
        else:
            raise Exception('Impossible situation!')

    # Binary search on column
    column = list(range(8))
    for char in rawDataLine[7:]:
        if char == 'L':
            column = BinarySplit(column, True)
        elif char == 'R':
            column = BinarySplit(column, False)
        else:
            raise Exception('Impossible situation!')

    # Calculate and save the seat ID at that row and column
    seatIDs.append(rows[0]*8+column[0])

seatIDs.sort()
print('Highest seat ID: ' + str(seatIDs[-1]))

# Find your missing seat ID
index = 1
while seatIDs[index-1] == seatIDs[index]-1:
    index += 1
print(seatIDs[index-2:index+2])
    