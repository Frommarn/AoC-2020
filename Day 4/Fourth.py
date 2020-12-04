# read in all data
# with open("Day 4/Testdata.txt",'r') as file:
with open("Day 4/Indata.txt",'r') as file:
    rawData = file.read()

rawDataLines = rawData.splitlines()

# print(rawDataLines)
class Passport(object):
    """
    A class for storing and manipulating information about a passport.
    """
    def __init__(self):
        self.rawData = []
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
    
    def AddRawData(self, rawString):
        """
        Add raw data to the passport
        """
        self.rawData.extend(rawString.split(' '))

    def PrintData(self):
        """
        Print the data
        """
        print(self.byr)
        print(self.iyr)
        print(self.eyr)
        print(self.hgt)
        print(self.hcl)
        print(self.ecl)
        print(self.pid)
        print(self.cid)

    def ParseRawData(self):
        """
        Parse the raw data into variables
        """
        for item in self.rawData:
            if item.startswith('byr'):
                self.byr = item[4:]
            elif item.startswith('iyr'):
                self.iyr = item[4:]
            elif item.startswith('eyr'):
                self.eyr = item[4:]
            elif item.startswith('hgt'):
                self.hgt = item[4:]
            elif item.startswith('hcl'):
                self.hcl = item[4:]
            elif item.startswith('ecl'):
                self.ecl = item[4:]
            elif item.startswith('pid'):
                self.pid = item[4:]
            elif item.startswith('cid'):
                self.cid = item[4:]
            else:
                raise Exception('Impossible state!')
    
    def Validate(self):
        """
        Validate the Passport
        """
        if self.byr == None:
            return False
        if self.iyr == None:
            return False
        if self.eyr == None:
            return False
        if self.hgt == None:
            return False
        if self.hcl == None:
            return False
        if self.ecl == None:
            return False
        if self.pid == None:
            return False
        # if self.cid == None:
        #     return False
        return True


# Collect raw data for each Passport in single string in a list
passports = []
currentPassport = Passport()
passports.append(currentPassport)
for line in rawDataLines:
    if line == '':
        currentPassport = Passport()
        passports.append(currentPassport)
    else:
        currentPassport.AddRawData(line)

nrValidPassports = 0
for passport in passports:
    passport.ParseRawData()
    if passport.Validate():
        nrValidPassports += 1

print(nrValidPassports)

# Parse every string into its own Passport object (class with properties)


# Iterate over Passport objects and count all valid ones
