# with open("Day 6/Testdata.txt",'r') as file:
with open("Day 6/Indata.txt",'r') as file:
    rawData = file.read()

rawDataLines = rawData.splitlines()

# Group each groups answers in its own set
groupAnswers = [set()]
for rawDataLine in rawDataLines:
    if rawDataLine == '':
        groupAnswers.append(set())
    else:
        for char in rawDataLine:
            groupAnswers[-1].add(char)

# Count unique answers in each group
count = 0
for group in groupAnswers:
    count += len(group)

print('Sum of unique answers per group: ' + str(count))