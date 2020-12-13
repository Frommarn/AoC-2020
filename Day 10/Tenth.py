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

# Nr of 1s, 2s & 3s
joltageDistribution = [0,0,0]

for index in range(len(adapterJoltages) - 1):
    joltageDifference = adapterJoltages[index + 1] - adapterJoltages[index]
    joltageDistribution[joltageDifference - 1] += 1

print('joltage distribution: ' + str(joltageDistribution))
print('1s times 3s: ' + str(joltageDistribution[0] * joltageDistribution[2]))