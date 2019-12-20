def readLines(file):
    with open(file) as f:
        content = f.readlines()
        content = [line.strip() for line in content]
    return content


def read(file):
    with open(file) as f:
        content = f.read()
    return content
