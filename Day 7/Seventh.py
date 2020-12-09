import collections as col

# with open("Day 7/Testdata.txt",'r') as file:
with open("Day 7/Indata.txt",'r') as file:
    rawData = file.read()

rawDataLines = rawData.splitlines()

# Cleanup the raw data into namedTuples
    # Example input:
    # bright white bags contain 1 shiny gold bag.
    # muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    # faded blue bags contain no other bags.

ChildTuple = col.namedtuple('ChildTuple', ['count', 'name'])

# Set up a dictionary with all mappings as namedTuples
bagDict = dict()
for rawDataLine in rawDataLines:
    name = ' '.join(rawDataLine.split(' ')[:2])
    if rawDataLine.endswith('no other bags.'):
        bagDict[name] = None
    else:
        childs = []
        for rawChild in ' '.join(rawDataLine.split(' ')[4:]).split(','):
            rawChild = rawChild.strip().split(' ')
            childCount = int(rawChild[0])
            childName = rawChild[1] + ' ' + rawChild[2]
            child = ChildTuple(childCount, childName)
            childs.append(child)
        bagDict[name] = childs


# Recursively traverse each "bag tree" looking for Shiny Gold bag
def Traverse(bagName):
    """
    Recursive method that looks for shiny gold bags in a "bag tree"
    """
    # Base case: Check if the current bag contains any shiny gold bags
    if bagDict[bagName] == None:
        return False
    for bag in bagDict[bagName]:
        if bag.name == 'shiny gold':
            return True
    
    # Recursive case: Check if any of the contained bags in turn contain any shiny gold bags
    for bag in bagDict[bagName]:
        if Traverse(bag.name) == True:
            return True
    
    # Default case: This bag and none of its contained bags contain any shiny gold bags
    return False

count = 0
for bag in bagDict.keys():
    result = Traverse(bag)
    if result == True:
        count += 1

print('Number of bags eventually containing shiny gold bags: ' + str(count))
# Profit!