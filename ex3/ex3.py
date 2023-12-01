import sys
def main():

    lines = []
    for line in sys.stdin:
        if '' == line.rstrip():
            break
        lines.append(line.rstrip('\n'))

    dict = {}
    for line in lines:
        dict[line[0]] = []
    for line in lines:
        dict[line[0]].append(line[2])
    exit(max(dict, key=dict.get))


if __name__ == "__main__":
    main()