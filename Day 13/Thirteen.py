# with open("Day 13/Testdata.txt",'r') as file:
with open("Day 13/Indata.txt",'r') as file:
    rawData = file.read().splitlines()

arrivingTimestamp = int(rawData[0])
print(arrivingTimestamp)
filteredRawData = list(filter(lambda raw: not raw == 'x', rawData[1].split(',')))
mapping = lambda raw: (raw, int(arrivingTimestamp / raw) * raw + raw - arrivingTimestamp)
sortedBusTuples = sorted(list(map(mapping, list(map(int,filteredRawData)))), key=lambda tuple: tuple[1])
earliestBus = sortedBusTuples[0]
print('Bus ID times timestamp diff: ' + str(earliestBus[0] * earliestBus[1]))