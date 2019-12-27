import file
instructions = file.read('inputs/day05.txt').split(',')


def getParams(intcode, pointer, modes):
    mode_a = modes.pop() if len(modes) > 0 else 0
    mode_b = modes.pop() if len(modes) > 0 else 0

    a = intcode[pointer + 1] if mode_a == 1 else intcode[intcode[pointer + 1]]
    b = intcode[pointer + 2] if mode_b == 1 else intcode[intcode[pointer + 2]]
    c = intcode[pointer + 3] if pointer + 3 < len(intcode) else None

    return (a, b, c)


def runTest(intcode, input):
    pointer = 0
    output = []

    while intcode[pointer] != 99:
        instruction = str(intcode[pointer])
        opcode, modes = int(
            instruction[-2:]), list(map(int, instruction[:-2]))

        if opcode == 1:
            a, b, c = getParams(intcode, pointer, modes)
            intcode[c] = a + b
        elif opcode == 2:
            a, b, c = getParams(intcode, pointer, modes)
            intcode[c] = a * b
        elif opcode == 3:
            inputPosition = intcode[pointer + 1]
            intcode[inputPosition] = input
        elif opcode == 4:
            outputPosition = intcode[pointer + 1]
            output.append(intcode[outputPosition])
        elif opcode == 5:
            a, b, _ = getParams(intcode, pointer, modes)
            if a != 0:
                pointer = b
                continue
        elif opcode == 6:
            a, b, _ = getParams(intcode, pointer, modes)
            if a == 0:
                pointer = b
                continue
        elif opcode == 7:
            a, b, c = getParams(intcode, pointer, modes)
            intcode[c] = 1 if a < b else 0
        elif opcode == 8:
            a, b, c = getParams(intcode, pointer, modes)
            intcode[c] = 1 if a == b else 0
        else:
            print('Unknown opcode: {}'.format(opcode))
            return [999]

        if opcode == 3 or opcode == 4:
            pointer += 2
        elif opcode == 5 or opcode == 6:
            pointer += 3
        else:
            pointer += 4

    return output


intcode = [int(num) for num in instructions]
print('Part One: {}'.format(runTest(intcode, 1)[-1]))

intcode = [int(num) for num in instructions]
print('Part Two: {}'.format(runTest(intcode, 5)[-1]))
