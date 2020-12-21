from datetime import datetime

# with open("Day 13/Testdata.txt",'r') as file:
with open("Day 13/Indata.txt",'r') as file:
    rawData = file.read().splitlines()

# Part 1
arrivingTimestamp = int(rawData[0])
print(arrivingTimestamp)
filteredRawData = list(filter(lambda raw: not raw == 'x', rawData[1].split(',')))
mapping = lambda raw: (raw, int(arrivingTimestamp / raw) * raw + raw - arrivingTimestamp)
sortedBusTuples = sorted(list(map(mapping, list(map(int,filteredRawData)))), key=lambda tuple: tuple[1])
earliestBus = sortedBusTuples[0]
print('Bus ID times timestamp diff: ' + str(earliestBus[0] * earliestBus[1]))


# Part 2
# with open("Day 13/Testdata.txt",'r') as file:
# with open("Day 13/Testdata2.txt",'r') as file:
# with open("Day 13/Testdata3.txt",'r') as file:
# with open("Day 13/Testdata4.txt",'r') as file:
with open("Day 13/Testdata5.txt",'r') as file:
# with open("Day 13/Testdata6.txt",'r') as file:
    rawDataPart2 = file.read()
# with open("Day 13/Indata.txt",'r') as file:
#     rawDataPart2 = file.read().splitlines()[1]

print('\n')
# busIDs = rawData[1].split(',')

rawBusData = rawDataPart2.split(',')
busIDTuples = []
for index in range(len(rawBusData)):
    if rawBusData[index] != 'x':
        busIDTuples.append((int(rawBusData[index]), index))

print(busIDTuples)
busIDTuples.sort(key=lambda tuple: tuple[0], reverse=True)
print(busIDTuples)
largestBusID = busIDTuples[0]
busIDTuples = list(map(lambda tuple: (tuple[0], tuple[1] - largestBusID[1]) , busIDTuples))
print(busIDTuples)

# Solve it using equations in a matrix
# timeStamp = 
# (t + delta) % busID = 0



timeStamp = 100000000000000
checkPointValue = 1000000000
# 1000000000
# 10000000000 <-- ~20s
# 100000000000000
checkPoint = checkPointValue + timeStamp
startTime = datetime.now()
# print(startTime)
while True:
    if timeStamp > checkPoint:
        print('Checkpoint ' + str(checkPoint) + ' : ' + str(datetime.now() - startTime))
        checkPoint += checkPointValue
    # if checkPoint >= 1000000000:
    #     break

    # Take the largest busID for each increment of timeStamp
    timeStamp += busIDTuples[0][0]
    for busTuple in busIDTuples:
        if (timeStamp + busTuple[1]) % busTuple[0] != 0:
            break
    # for index in indexes:
    #     if (timeStamp + index) % busIDs[index] != 0:
    #         break
    else:
        # Found the matching 
        print('timeStamp: ' + str(timeStamp))

        # End infinite loop
        break
print(datetime.now() - startTime)



# busIDs = list(map(lambda raw: 1 if raw == 'x' else int(raw), rawDataPart2.split(',')))

# timeStamp = 0
# indexes = range(len(busIDs))
# checkPoint = checkPointValue
# startTime = datetime.now()
# # print(datetime.now())
# while True:
#     if timeStamp > checkPoint:
#         print('Checkpoint ' + str(checkPoint) + ' : ' + str(datetime.now() - startTime))
#         checkPoint += checkPointValue
#     if checkPoint >= 1000000000:
#         break

#     # Take the largest busID for each increment of timeStamp
#     timeStamp += busIDs[0]
#     for index in indexes:
#         if (timeStamp + index) % busIDs[index] != 0:
#             break
#     else:
#         # Found the matching 
#         print('timeStamp: ' + str(timeStamp))

#         # End infinite loop
#         break
# print(datetime.now() - startTime)



# def Recurse(timestamp, buses):
#     """
#     Recursive method for validating the buses
#     """
#     # Base case: Empty list
#     if len(buses) == 0:
#         return True
    
#     # Base case: First bus is 'x'
#     if buses[0] == 'x':
#         return Recurse(timestamp + 1, buses[1:])
    
#     # Recursive case: Check if first bus in list matches timestamp
#     if timestamp % int(buses[0]) == 0:
#         return Recurse(timestamp + 1, buses[1:])
#     else:
#         return False

# # timeStamp = 100000000000000
# timeStamp = 0
# startTimeStamp = None
# print(datetime.now())
# while True:
#     startTimeStamp = timeStamp
#     if Recurse(timeStamp, busIDs):
#         print('TimeStamp: ' + str(startTimeStamp))
#         break
#     else:
#         newTimeStamp = timeStamp + int(busIDs[0])
#         if newTimeStamp < startTimeStamp:
#             print('Overflow!')
#             break
#         else:
#             timeStamp = newTimeStamp

# print(datetime.now())
# print('Ended')

