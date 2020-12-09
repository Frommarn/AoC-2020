# with open("Day 9/Testdata.txt",'r') as file:
with open("Day 9/Indata.txt",'r') as file:
    rawData = file.read()

rawDataLines = rawData.splitlines()
numbers = list(map(int,rawDataLines))

preAmble = 25

def Validate(number, previousNumbers):
    """
    Validates if the given number is a sum of two different previous numbers.
    """
    for i in range(len(previousNumbers) - 1):
        for j in range(i + 1, len(previousNumbers)):
            if previousNumbers[i] + previousNumbers[j] == number:
                return True
    
    return False

indexOfFirstIncorrect = None
firstIncorrectNumber = None
for index in range(preAmble, len(numbers)):
    previousNumbers = numbers[index - preAmble:index]
    number = numbers[index]
    isOK = Validate(number, previousNumbers)
    if not isOK:
        indexOfFirstIncorrect = index
        firstIncorrectNumber = numbers[index]
        print('Index: ' + str(indexOfFirstIncorrect) + ', Number: ' + str(firstIncorrectNumber))
        break

def Counter(startIndex, targetSum):
    """
    Sum one item at a time starting from the given index until either matching targetSum (sublist of summed numbers) or exceeds it (False)
    """
    count = 0
    currIndex = startIndex
    while True:
        count += numbers[currIndex]
        currIndex += 1
        if count == targetSum:
            return numbers[startIndex:currIndex]
        elif count > targetSum:
            return False
        else:
            continue

for index in range(len(numbers) - 1):

    result = Counter(index, firstIncorrectNumber)
    if result == False:
        continue
    else:
        print(result)
        result.sort()
        print(result)
        sum = result[0] + result[-1]
        print(str(sum))
        break
