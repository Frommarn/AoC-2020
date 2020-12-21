import cmath
import math

# with open("Day 12/Testdata.txt",'r') as file:
with open("Day 12/Indata.txt",'r') as file:
    rawData = file.read()

instructions = list(map(lambda raw: (raw[0], int(raw[1:])), rawData.splitlines()))

shipPos = complex(0, 0)
wayPointPos = complex(10, 1)

for instruction in instructions:
    if instruction[0] == 'N':
        wayPointPos = wayPointPos + complex(0, instruction[1])
    elif instruction[0] == 'S':
        wayPointPos = wayPointPos - complex(0, instruction[1])
    elif instruction[0] == 'E':
        wayPointPos = wayPointPos + complex(instruction[1], 0)
    elif instruction[0] == 'W':
        wayPointPos = wayPointPos - complex(instruction[1], 0)
    elif instruction[0] == 'L':
        degrees = instruction[1]
        while degrees > 0:
            degrees -= 90
            wayPointPos = wayPointPos * complex(0, 1)
    elif instruction[0] == 'R':
        degrees = instruction[1]
        while degrees > 0:
            degrees -= 90
            wayPointPos = wayPointPos * complex(0, -1)
    elif instruction[0] == 'F':
        nrOfHops = instruction[1]
        while nrOfHops > 0:
            nrOfHops -= 1
            shipPos = shipPos + wayPointPos
    else:
        raise Exception('The impossible happened!')

print('horizontal count: ' + str(shipPos.real))
print('Vertical count: ' + str(shipPos.imag))
print('Manhattan distance: ' + str(abs(shipPos.real) + abs(shipPos.imag)))