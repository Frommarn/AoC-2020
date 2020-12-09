import collections as col

# with open("Day 8/Testdata.txt",'r') as file:
with open("Day 8/Indata.txt",'r') as file:
    rawData = file.read()

rawDataLines = rawData.splitlines()

# Cleanup the raw data into namedTuples
InstructionTuple = col.namedtuple('InstructionTuple', ['operation', 'argument'])
instructions = []
for rawDataLine in rawDataLines:
    operation, argument = rawDataLine.split(' ')
    instructions.append(InstructionTuple(operation, int(argument)))

# Run the simulator and track which instructions have been executed
accumulator = 0
visitedInstructions = [0] * len(instructions)

nextInstructionIndex = 0
while True:
    # If we have already executed the next instruction, stop the simulation
    if visitedInstructions[nextInstructionIndex] == 1:
        break
    else:
        nextInstruction = instructions[nextInstructionIndex]
        visitedInstructions[nextInstructionIndex] = 1
        if nextInstruction.operation == 'acc':
            accumulator += nextInstruction.argument
            nextInstructionIndex += 1
        elif nextInstruction.operation == 'jmp':
            nextInstructionIndex += nextInstruction.argument
        elif nextInstruction.operation == 'nop':
            nextInstructionIndex += 1
        else:
            raise Exception('The impossible happened!')

print('accumulator at start of infinite loop: ' + str(accumulator))