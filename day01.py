import math
import file

moduleMasses = file.readLines('inputs/day01.txt')


def calcFuel(mass):
    return math.floor(float(mass) / 3) - 2


def partOne():
    totalFuel = 0
    for moduleMass in moduleMasses:
        totalFuel += calcFuel(moduleMass)
    return totalFuel


def partTwo():
    totalFuel = 0
    for moduleMass in moduleMasses:
        fuel = moduleMass
        while True:
            fuel = calcFuel(fuel)
            if fuel > 0:
                totalFuel += fuel
            else:
                break
    return totalFuel


print("Part 1: %d" % partOne())
print("Part 2: %d" % partTwo())
