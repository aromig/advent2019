import file

input = file.read('inputs/day02.txt')

HALT = 99
ADD = 1
MULT = 2

input = input.split(',')


def runInstructions(intcode):
    pointer = 0
    while intcode[pointer] != HALT:
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

    return intcode


def partOne():
    intcode = [int(num) for num in input]
    intcode[1] = 12
    intcode[2] = 2

    return runInstructions(intcode)[0]


def partTwo():
    for noun in range(0, 99):
        for verb in range(0, 99):
            intcode = [int(num) for num in input]
            intcode[1] = noun
            intcode[2] = verb
            if runInstructions(intcode)[0] == 19690720:
                return 100 * noun + verb


print("Part 1: %d" % partOne())
print("Part 2: %d" % partTwo())
