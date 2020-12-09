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

for index in range(preAmble, len(numbers)):
    previousNumbers = numbers[index - preAmble:index]
    number = numbers[index]
    isOK = Validate(number, previousNumbers)
    if not isOK:
        print(numbers[index])
        break