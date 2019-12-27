import file
orbits = file.readLines('inputs/day06.txt')

# Prep planet/orbit list

for num in range(len(orbits)):
    orbits[num] = orbits[num].split(')')

orbit_list = []

for x in range(len(orbits)):
    for y in range(len(orbits[x])):
        orbit_list.append(orbits[x][y])

planets = list(set(orbit_list))

for num in range(len(planets)-1):
    if (planets[num] == "COM"):
        del(planets[num])


# Part One


def getOrbits_P1(orbitList, planet, count):
    result = 0
    for orbit in orbitList:
        orbitCount = count
        end = orbit[0]
        planetCheck = orbit[1]

        if (planetCheck == planet):
            if (end != "COM"):
                orbitCount += 1
                result = getOrbits_P1(orbitList, end, orbitCount)
            else:
                orbitCount += 1
                result = orbitCount

    return result


totalCount = 0

for planet in planets:
    num = getOrbits_P1(orbits, planet, 0)
    totalCount += num

print("Part One: %d" % totalCount)


# Part Two


def getOrbits_P2(orbitList, planet, planetList):
    for orbit in orbitList:
        subList = planetList
        end = orbit[0]
        planetCheck = orbit[1]

        if (planetCheck == planet):
            if (end != "COM"):
                subList.append(orbit)
                result = getOrbits_P2(orbitList, end, subList)
            else:
                subList.append(orbit)
                result = subList
                break

    return result


def getTransfers(list1, list2):
    count = 0

    for x in list1:
        for y in list2:
            if (x[0] == y[0] and x != y):
                count = list1.index(x) + list2.index(y)

    return count


you = []
san = []

you = getOrbits_P2(orbits, "YOU", you)
san = getOrbits_P2(orbits, "SAN", san)

print("Part Two: %d" % getTransfers(you, san))
