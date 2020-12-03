import collections as col

# read in all data
# with open("Day 2/Testdata.txt",'r') as file:
with open("Day 2/Indata.txt",'r') as file:
    rawData = file.read()

# split data into tuples:
# Example input: 1-3 a: abcde
# Split into tuple: {lowest, highest, char, password}
PasswordRule = col.namedtuple('PasswordRule', ['lowest', 'highest', 'char', 'password'])

def ParsePasswords(raw):
    """
    Method which parses raw data into a named tuple.
    """
    rawSplit = raw.replace('-', ' ').replace(':', ' ').split()
    p = PasswordRule(int(rawSplit[0]), int(rawSplit[1]),rawSplit[2],rawSplit[3])
    return p

passwords = list(map(ParsePasswords, rawData.splitlines()))

# iterate over each tuple and validate it

def ValidatePassword(passTuple):
    """
    Validates the password tuple according to its rules
    """
    nrOccurences = passTuple.password.count(passTuple.char)
    if passTuple.lowest <= nrOccurences <= passTuple.highest :
        isValid = True
    else:
        isValid = False
    return isValid

count = 0
for p in passwords:
    if ValidatePassword(p):
        count = count + 1
print("Number of valid passwords:" + str(count))