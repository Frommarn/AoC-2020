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

isSuccess = False
for index in range(len(instructions)):
    if instructions[index].operation not in ['nop', 'jmp']:
        continue

    # Run the simulator and track which instructions have been executed
    accumulator = 0
    visitedInstructions = [0] * len(instructions)
    modifiedInstructions = instructions.copy()

    # Modify nop/jmp instruction
    tmp = modifiedInstructions[index]
    if tmp.operation == 'nop':
        modifiedInstructions[index] = InstructionTuple('jmp', tmp.argument)
    elif tmp.operation == 'jmp':
        modifiedInstructions[index] = InstructionTuple('nop', tmp.argument)
    else:
        raise Exception('The impossible happened!')

    nextInstructionIndex = 0
    while True:
        # If we try to execute exactly one step outside the instruction list, we fixed the program!
        if nextInstructionIndex == len(modifiedInstructions):
            isSuccess = True
            print('Success!')
            break
        # If we try to execute more than one step outside the instruction list, we broke something
        elif nextInstructionIndex > len(modifiedInstructions):
            print('We overshot!')
            break
        # If we try to execute on a negative index on the instruction list, we broke something
        elif nextInstructionIndex < 0:
            print('Negative index!')
            break
        # If we have already executed the next instruction, stop the simulation
        elif visitedInstructions[nextInstructionIndex] == 1:
            break
        else:
            nextInstruction = modifiedInstructions[nextInstructionIndex]
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
    
    if isSuccess:
        print('accumulator at start of infinite loop: ' + str(accumulator))
        break
