import file
instructions = file.read('inputs/day05.txt').split(',')

HALT = 99
ADD = 1
MULT = 2
INPUT = 3
OUTPUT = 4

POSITION_MODE = 0
IMMEDIATE_MODE = 1


def runInstructions(intcode, input):
    pointer = 0
    while intcode[pointer] != HALT or pointer > len(intcode):
        if len(str(intcode[pointer])) == 1:
            if intcode[pointer] == INPUT:
                inputAddress = intcode[intcode.index(INPUT) + 1]
                intcode[inputAddress] = input
                pointer += 2
            elif intcode[pointer] == OUTPUT:
                outputAddress = intcode[pointer + 1]
                print(intcode[outputAddress])
                pointer += 2
            else:
                pos_1 = intcode[pointer + 1]
                val_1 = intcode[pos_1]
                pos_2 = intcode[pointer + 2]
                val_2 = intcode[pos_2]
                store = intcode[pointer + 3]

                if intcode[pointer] == ADD:
                    intcode[store] = val_1 + val_2
                if intcode[pointer] == MULT:
                    intcode[store] = val_1 * val_2
                pointer += 4

        else:
            instruction = str(intcode[pointer])
            instruction = instruction.zfill(5)
            opcode = int(instruction[-2:])
            mode_1 = int(instruction[-3:-2])
            mode_2 = int(instruction[-4:-3])
            mode_3 = int(instruction[-5:-4])

            if opcode == OUTPUT:
                if mode_1 == 0:
                    print(intcode[pointer + 1])
                if mode_2 == 1:
                    outputAddress = intcode[pointer + 1]
                    print(intcode[outputAddress])
                skip = 2
            else:
                if mode_1 == 0:
                    pos_1 = intcode[pointer + 1]
                    val_1 = intcode[pos_1]
                if mode_1 == 1:
                    val_1 = intcode[pointer + 1]
                if mode_2 == 0:
                    pos_2 = intcode[pointer + 2]
                    val_2 = intcode[pos_2]
                if mode_2 == 1:
                    val_2 = intcode[pointer + 2]
                if mode_3 == 0:
                    store = intcode[pointer + 3]

                if opcode == ADD:
                    intcode[store] = val_1 + val_2
                if opcode == MULT:
                    intcode[store] = val_1 * val_2

                skip = 4

            pointer += skip

    return intcode


def getInputAddress(intcode):
    return intcode[intcode.index(INPUT) + 1]


def partOne():
    print("Part One:")
    intcode = [int(num) for num in instructions]
    return runInstructions(intcode, 1)


partOne()
