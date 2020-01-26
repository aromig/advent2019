import file
instructions = file.read('inputs/day09.txt').split(',')

def getParams(opcode, intcode, pointer, modes, rel_base):
    ref = 0

    mode_a = modes.pop() if len(modes) > 0 else 0
    mode_b = modes.pop() if len(modes) > 0 else 0
    mode_c = modes.pop() if len(modes) > 0 else 0

    param_a = intcode[pointer + 1]
    param_b = intcode[pointer + 2]
    param_c = intcode[pointer + 3]

    if mode_a == 1:
        ref = pointer + 1
        a = intcode[ref]
    elif mode_a == 2:
        a = intcode[rel_base + param_a] if opcode != 3 else rel_base + param_a
    else:
        ref = param_a if opcode != 3 else pointer + 1
        a = intcode[ref]

    if mode_b == 1:
        ref = pointer + 2
    elif mode_b == 2:
        ref = rel_base + param_b
    else:
        ref = param_b
    b = intcode[ref]

    c = param_c if mode_c == 0 else rel_base + param_c


    return (a, b, c)


def runTest(intcode, input):
    pointer = 0
    output = []
    relative_base = 0

    while intcode[pointer] != 99:
        instruction = str(intcode[pointer])
        opcode, modes = int(
            instruction[-2:]), list(map(int, instruction[:-2]))

        a, b, c = getParams(opcode, intcode, pointer, modes, relative_base)

        if opcode == 1:
            intcode[c] = a + b
        elif opcode == 2:
            intcode[c] = a * b
        elif opcode == 3:
            intcode[a] = input
        elif opcode == 4:
            print(a)
            output.append(a)
        elif opcode == 5:
            if a != 0:
                pointer = b
                continue
        elif opcode == 6:
            if a == 0:
                pointer = b
                continue
        elif opcode == 7:
            intcode[c] = 1 if a < b else 0
        elif opcode == 8:
            intcode[c] = 1 if a == b else 0
        elif opcode == 9:
            relative_base = relative_base + a
        else:
            print('Unknown opcode: {}'.format(opcode))
            return [999]

        if opcode == 3 or opcode == 4 or opcode == 9:
            pointer += 2
        elif opcode == 5 or opcode == 6:
            pointer += 3
        else:
            pointer += 4

    return output[-1]

intcode = [int(num) for num in instructions]
extra = [0 for n in range(0, 50000)]
intcode.extend(extra)
print('Part One: {}'.format(runTest(intcode, 1)))

intcode = [int(num) for num in instructions]
extra = [0 for n in range(0, 50000)]
intcode.extend(extra)
print('Part Two: {}'.format(runTest(intcode, 2)))