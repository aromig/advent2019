import math
import file
raw = file.readLines('inputs/day10.txt')

def find_asteroids():
    for y, line in enumerate(raw):
        for x, a in enumerate(line):
            if a == '#':
                yield (x, y)

def get_angle(start, end):
    angle = math.atan2(end[0] - start[0], start[1] - end[1]) * 180 / math.pi
    if angle < 0:
        return 360 + angle
    return angle

def partOne(asteroids):
    location = None
    max_count = 0

    for start in asteroids:
        count = len({get_angle(start, end) for end in asteroids if start != end})
        if count > max_count:
            max_count = count
            location = start
   
    return location, max_count

def partTwo(asteroids, station_loc):
    asteroids.remove(station_loc)
    asteroid_angles = sorted(
        ((get_angle(station_loc, end), end) for end in asteroids),
            key=lambda x: (x[0], abs(station_loc[0] - x[1][0]) + abs(station_loc[1] - x[1][1]))
    )

    index = 0
    current = asteroid_angles.pop(index)
    last = current[0]
    count = 1

    while count < 200 and asteroid_angles:
        if index >= len(asteroid_angles):
            index = 0
            last = None
        if last == asteroid_angles[index][0]:
            index += 1
            continue
        current = asteroid_angles.pop(index)
        last = current[0]
        count += 1
    
    return current[1], current[1][0] * 100 + current[1][1]

asteroids = list(find_asteroids())
station_location, num_asteroids = partOne(asteroids)

print('Part 1:')
print('Best location @ x {} y {}'.format(*station_location))
print('# Asteroids in view: {}'.format(num_asteroids))

x, y = partTwo(asteroids, station_location)
print('Part 2:')
print('Vaporized 200th @ {} -> {}'.format(x, y))