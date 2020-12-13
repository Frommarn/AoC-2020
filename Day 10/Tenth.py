from datetime import datetime
from functools import reduce

# with open("Day 10/Testdata.txt",'r') as file:
# with open("Day 10/Testdata2.txt",'r') as file:
with open("Day 10/Indata.txt",'r') as file:
    rawData = file.read()

rawDataLines = rawData.splitlines()
adapterJoltages = list(map(int,rawDataLines))

# Append charging outlet joltage of 0
adapterJoltages.append(0)
adapterJoltages.sort()

# Append device built-in joltage adapter
adapterJoltages.append(adapterJoltages[-1] + 3)

print(adapterJoltages)

highEnd3DifferenceNumbers = []

# Nr of 1s, 2s & 3s
joltageDistribution = [0,0,0]

for index in range(len(adapterJoltages) - 1):
    joltageDifference = adapterJoltages[index + 1] - adapterJoltages[index]
    if joltageDifference == 3:
        highEnd3DifferenceNumbers.append(adapterJoltages[index + 1])
    joltageDistribution[joltageDifference - 1] += 1

print('joltage distribution: ' + str(joltageDistribution))
print('1s times 3s: ' + str(joltageDistribution[0] * joltageDistribution[2]))

# Part 2

# Recurse removing one element at a time and re-validating the setup
# Return the number of correct setups

print('\n')
validSetups = dict()

def Recurse(setup, ignoreFirst, ignoreLast):
    # Base case: already checked?
    stringify = ''.join(str(setup))
    if stringify in validSetups:
        return 0

    # Base case: validate the setup
    isValid = True
    for index in range(len(setup) - 1):
        if not (4 > setup[index + 1] - setup[index] > 0):
            isValid = False
            break
    if isValid:
        validSetups[stringify] = True
    else:
        return 0

    # Recursive case: remove one element at a time (if valid setup)
    nrOfValidSetups = 0
    if isValid:
        # print(setup)
        nrOfValidSetups += 1
        startIndex = 1
        if ignoreFirst:
            startIndex = 0
        stopIndex = 2
        if ignoreLast:
            stopIndex = 1
        for index in range(startIndex, len(setup) - stopIndex, 1):
            if 4 > setup[index + 1] - setup[index - 1] > 0:
                subSetup = setup.copy()
                del subSetup[index]
                nrOfValidSetups += Recurse(subSetup, ignoreFirst, ignoreLast)
            else:
                # Not a valid removal, pass
                pass

    # Default case: return count of valid setups
    return nrOfValidSetups

print(datetime.now())
resultParts = []

# Get starting special case
endSubIndex = adapterJoltages.index(highEnd3DifferenceNumbers[0])
firstPart = adapterJoltages[:endSubIndex]
resultPart = Recurse(firstPart, False, True)
resultParts.append(resultPart)
# Middle cases
for index in range(len(highEnd3DifferenceNumbers) - 1):
    startSubIndex = adapterJoltages.index(highEnd3DifferenceNumbers[index])
    endSubIndex = adapterJoltages.index(highEnd3DifferenceNumbers[index + 1])
    adapterJoltagesPart = adapterJoltages[startSubIndex:endSubIndex]
    resultPart = Recurse(adapterJoltagesPart, True, True)
    resultParts.append(resultPart)

# Get ending special case
startSubIndex = adapterJoltages.index(highEnd3DifferenceNumbers[-1])
firstPart = adapterJoltages[startSubIndex:]
resultPart = Recurse(firstPart, True, False)
resultParts.append(resultPart)

finalResult = reduce((lambda x, y: x * y), resultParts)
print(datetime.now())
print(str(finalResult))

