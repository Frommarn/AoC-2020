# with open("Day 11/Testdata.txt",'r') as file:
with open("Day 11/Indata.txt",'r') as file:
    rawData = file.read()

seatRows = rawData.splitlines()
nrOfRows = len(seatRows)
rowLength = len(seatRows[0])

def PrintSeats(seats):
    for row in seats:
        print(row)

def LineOfSight(verticalDirection, horizontalDirection, rowIndex, index, inputSeats):
    # Traverse to next in line
    rowIndex += verticalDirection
    index += horizontalDirection

    # Base cases: If out of range, no seat was found
    if rowIndex < 0 or nrOfRows <= rowIndex:
        return False
    if index < 0 or rowLength <= index:
        return False
    
    # Recursive case: Check current seat, if '.', recurse
    if inputSeats[rowIndex][index] == '#':
        return True
    elif inputSeats[rowIndex][index] == 'L':
        return False
    else:
        return LineOfSight(verticalDirection, horizontalDirection, rowIndex, index, inputSeats)

def CountNeighbouring(rowIndex, index, inputSeats):
    nrOfOccupied = 0
    isLeftOK = True if index - 1 >= 0 else False
    isRightOK = True if index + 1 < rowLength else False
    isTopOK = True if rowIndex - 1 >= 0 else False
    isBottomOK = True if rowIndex + 1 < nrOfRows else False

    # Check top left
    if isLeftOK and isTopOK and LineOfSight(-1, -1, rowIndex, index, inputSeats):
        nrOfOccupied += 1
    # Check top middle
    if isTopOK and LineOfSight(-1, 0, rowIndex, index, inputSeats):
        nrOfOccupied += 1
    # Check top right
    if isRightOK and isTopOK and LineOfSight(-1, 1, rowIndex, index, inputSeats):
        nrOfOccupied += 1
    # Check left
    if isLeftOK and LineOfSight(0, -1, rowIndex, index, inputSeats):
        nrOfOccupied += 1
    # Check right
    if isRightOK and LineOfSight(0, 1, rowIndex, index, inputSeats):
        nrOfOccupied += 1
    # Check bottom left
    if isLeftOK and isBottomOK and LineOfSight(1, -1, rowIndex, index, inputSeats):
        nrOfOccupied += 1
    # Check bottom middle
    if isBottomOK and LineOfSight(1, 0, rowIndex, index, inputSeats):
        nrOfOccupied += 1
    # Check bottom right
    if isRightOK and isBottomOK and LineOfSight(1, 1, rowIndex, index, inputSeats):
        nrOfOccupied += 1
    
    return nrOfOccupied

def Iterate(inputSeats):
    result = []
    for rowIndex in range(nrOfRows):
        rowResult = []
        for index in range(rowLength):
            currentSeat = inputSeats[rowIndex][index]
            nrOfOccupied = CountNeighbouring(rowIndex, index, inputSeats)
            if currentSeat == 'L' and nrOfOccupied == 0:
                rowResult.append('#')
            elif currentSeat == '#' and nrOfOccupied >= 5:
                rowResult.append('L')
            else:
                rowResult.append(currentSeat)
        result.append(''.join(rowResult))
    return result

def Count(inputSeats):
    nrOfOccupied = 0
    for rowIndex in range(nrOfRows):
        for index in range(rowLength):
            if inputSeats[rowIndex][index] == '#':
                nrOfOccupied += 1
    return nrOfOccupied

isSame = False
iterationCount = 1
while not isSame:
    print('Iteration: ' + str(iterationCount))
    iterationCount += 1
    # PrintSeats(seatRows)

    newSeats = Iterate(seatRows)
    if newSeats == seatRows:
        isSame = True
    else:
        seatRows = newSeats
        newSeats = []

count = Count(seatRows)
print('Count: ' + str(count))