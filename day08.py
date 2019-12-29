import file
import copy
raw = list(file.read('inputs/day08.txt'))


def partOne(raw_image, width, height):
    for i in range(len(raw_image)):
        raw_image[i] = int(raw_image[i])

    layer_size = width * height
    num_layers = len(raw_image) / layer_size
    layers = []
    current_layer = []

    for i in range(len(raw_image)):
        current_layer.append(raw_image[i])
        if (i + 1) % layer_size == 0:
            layers.append(copy.copy(current_layer))
            current_layer.clear()

    fewest_zeroes = len(raw_image) / (width * height)
    selected_layer = []

    for x in layers:
        count = 0
        for y in range(len(x)):
            if (x[y] == 0):
                count += 1
        if count < fewest_zeroes:
            fewest_zeroes = count
            selected_layer = x

    print("Layer " + str(layers.index(selected_layer)+1) +
          " has the fewest zeroes: " + str(fewest_zeroes))

    ones, twos = 0, 0

    for i in selected_layer:
        if i == 1:
            ones += 1
        elif i == 2:
            twos += 1

    print("It has %d ones" % ones)
    print("It has %d twos" % twos)
    print("\nPart One: %d" % (ones*twos))


def partTwo(raw_image, width, height):
    for i in range(len(raw_image)):
        raw_image[i] = int(raw_image[i])

    layer_size = width * height
    num_layers = len(raw_image) / layer_size
    layers = []
    current_layer = []
    image = []

    for i in range(len(raw_image)):
        current_layer.append(raw_image[i])
        if (i + 1) % layer_size == 0:
            layers.append(copy.copy(current_layer))
            current_layer.clear()

    # For each pixel, search each layer from top to bottom for first visible color
    # Break out to next pixel after finding black or white

    BLACK = 0
    WHITE = 1
    TRANSPARENT = 2

    for x in range(layer_size):
        for y in layers:
            if y[x] == TRANSPARENT:
                continue
            elif y[x] == WHITE:
                image.append('#')
                break
            elif y[x] == BLACK:
                image.append(" ")
                break

    # Print out the image

    print("Part Two:\n")

    for z in range(len(image)):
        if (z + 1) % width == 0:
            print(image[z])
        else:
            print(image[z], end=" ")


partOne(raw, 25, 6)

partTwo(raw, 25, 6)
