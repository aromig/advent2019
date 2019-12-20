import file

input = file.read('inputs/day03.txt')
paths = input.split('\n')

path_1 = paths[0].split(',')
path_2 = paths[1].split(',')


def calcPoints(path):
    x = 0
    y = 0
    step = 0
    directions = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)}
    points = {}

    for segment in path:
        dx, dy = directions[segment[0]]
        for _ in range(int(segment[1:])):
            x += dx
            y += dy
            step += 1
            if (x, y) not in points:
                points[(x, y)] = step

    return points


def partOne():
    points_1 = calcPoints(path_1)
    points_2 = calcPoints(path_2)

    points_intersected = [point for point in points_1 if point in points_2]

    return min(abs(x) + abs(y) for (x, y) in points_intersected)


def partTwo():
    points_1 = calcPoints(path_1)
    points_2 = calcPoints(path_2)

    points_intersected = [point for point in points_1 if point in points_2]

    return min(points_1[point] + points_2[point] for point in points_intersected)


print("Part 1: %d" % partOne())
print("Part 2: %d" % partTwo())
