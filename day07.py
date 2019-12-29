import file
from itertools import permutations
instructions = file.read('inputs/day07.txt').split(',')


def get_phase_perms(phases):
    phase_perms = [[]]
    for n in phases:
        new_perm = []
        for perm in phase_perms:
            for i in range(len(perm)+1):
                new_perm.append(perm[:i] + [n] + perm[i:])
                phase_perms = new_perm
    return phase_perms


def getParams(intcode, pointer, modes):
    mode_a = modes.pop() if len(modes) > 0 else 0
    mode_b = modes.pop() if len(modes) > 0 else 0

    a = intcode[pointer + 1] if mode_a == 1 else intcode[intcode[pointer + 1]]
    b = intcode[pointer + 2] if mode_b == 1 else intcode[intcode[pointer + 2]]
    c = intcode[pointer + 3] if pointer + 3 < len(intcode) else None

    return (a, b, c)


def runTest(intcode, inputs, is_feedback=False, pointer=0):
    output = []
    diag_code = 0

    while intcode[pointer] != 99:
        instruction = str(intcode[pointer])
        opcode, modes = int(
            instruction[-2:]), list(map(int, instruction[:-2]))

        if opcode == 1:
            a, b, c = getParams(intcode, pointer, modes)
            intcode[c] = a + b
            pointer += 4
        elif opcode == 2:
            a, b, c = getParams(intcode, pointer, modes)
            intcode[c] = a * b
            pointer += 4
        elif opcode == 3:
            inputPosition = intcode[pointer + 1]
            intcode[inputPosition] = inputs.pop(0)
            pointer += 2
        elif opcode == 4:
            outputPosition = intcode[pointer + 1]
            diag_code = intcode[outputPosition]
            output.append(diag_code)
            pointer += 2
            if is_feedback:
                return diag_code, pointer
        elif opcode == 5:
            a, b, _ = getParams(intcode, pointer, modes)
            if a != 0:
                pointer = b
                continue
            pointer += 3
        elif opcode == 6:
            a, b, _ = getParams(intcode, pointer, modes)
            if a == 0:
                pointer = b
                continue
            pointer += 3
        elif opcode == 7:
            a, b, c = getParams(intcode, pointer, modes)
            intcode[c] = 1 if a < b else 0
            pointer += 4
        elif opcode == 8:
            a, b, c = getParams(intcode, pointer, modes)
            intcode[c] = 1 if a == b else 0
            pointer += 4
        else:
            raise Exception('Unknown opcode: {}'.format(opcode))

    if is_feedback:
        return diag_code, None

    return output[-1]

# Part One


def partOne():
    max_signal = 0

    for phase_perm in get_phase_perms(range(0, 5)):
        program = [int(num) for num in instructions]
        output = 0
        while len(phase_perm) > 0:
            output = runTest(program, [phase_perm.pop(0), output])
        max_signal = max(max_signal, output)

    return max_signal


# Part Two


def run_loop(program, phases):
    programs, ptrs, inputs = [], [], []
    nAmps = len(phases)
    output = 0

    for i in range(0, nAmps):
        program_copy = program[:]
        programs.append(program_copy)
        ptrs.append(0)
        inputs.append([phases[i]])

    while ptrs[0] is not None:
        for i in range(0, nAmps):
            inputs[i].append(output)
            output, ptr = runTest(
                programs[i], inputs[i], True, ptrs[i])
            ptrs[i] = ptr
    return inputs[0][0]


def partTwo():
    program = [int(num) for num in instructions]
    max_signal = 0

    for phase_perm in get_phase_perms(range(5, 10)):
        max_signal = max(max_signal, run_loop(program, phase_perm))

    return max_signal


print("Part One: {}".format(partOne()))
print("Part Two: {}".format(partTwo()))
