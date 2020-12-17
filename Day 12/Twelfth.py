# with open("Day 12/Testdata.txt",'r') as file:
with open("Day 12/Indata.txt",'r') as file:
    rawData = file.read()

instructions = list(map(lambda raw: (raw[0], int(raw[1:])), rawData.splitlines()))

leftRotation = dict()
leftRotation['north'] = 'west'
leftRotation['west'] = 'south'
leftRotation['south'] = 'east'
leftRotation['east'] = 'north'

rightRotation = dict()
rightRotation['north'] = 'east'
rightRotation['east'] = 'south'
rightRotation['south'] = 'west'
rightRotation['west'] = 'north'

def Rotate(rotateDir, degrees, forwardDirection):
    if rotateDir == 'L':
        while degrees > 0:
            degrees -= 90
            forwardDirection = leftRotation[forwardDirection]
    elif rotateDir == 'R':
        while degrees > 0:
            degrees -= 90
            forwardDirection = rightRotation[forwardDirection]
    else:
        raise Exception('The impossible happened!')
    return forwardDirection

verticalCount = 0
horizontalCount = 0
forwardDirection = 'east'

for instruction in instructions:
    if instruction[0] == 'N':
        verticalCount += instruction[1]
    elif instruction[0] == 'S':
        verticalCount -= instruction[1]
    elif instruction[0] == 'E':
        horizontalCount += instruction[1]
    elif instruction[0] == 'W':
        horizontalCount -= instruction[1]
    elif instruction[0] == 'L':
        forwardDirection = Rotate(instruction[0], instruction[1], forwardDirection)
    elif instruction[0] == 'R':
        forwardDirection = Rotate(instruction[0], instruction[1], forwardDirection)
    elif instruction[0] == 'F':
        if forwardDirection == 'east':
            horizontalCount += instruction[1]
        elif forwardDirection == 'west':
            horizontalCount -= instruction[1]
        elif forwardDirection == 'north':
            verticalCount += instruction[1]
        elif forwardDirection == 'south':
            verticalCount -= instruction[1]
        else:
            raise Exception('The impossible happened!')
    else:
        raise Exception('The impossible happened!')

print('Vertical count: ' + str(verticalCount))
print('horizontal count: ' + str(horizontalCount))
print('Manhattan distance: ' + str(abs(verticalCount) + abs(horizontalCount)))