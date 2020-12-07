# with open("Day 6/Testdata.txt",'r') as file:
with open("Day 6/Indata.txt",'r') as file:
    rawData = file.read()

rawDataLines = rawData.splitlines()

# Group each groups answers in its own list where each person has a set of answers
groupAnswers = [[]]
for rawDataLine in rawDataLines:
    if rawDataLine == '':
        groupAnswers.append([])
    else:
        singleSet = set()
        for char in rawDataLine:
            singleSet.add(char)
        
        groupAnswers[-1].append(singleSet)

# Count unique answers in each group
count = 0
for group in groupAnswers:
    # Part 1
    # count += len(group)

    # Part 2
    count += len(set.intersection(*group))

print('Sum of unique answers per group: ' + str(count))
