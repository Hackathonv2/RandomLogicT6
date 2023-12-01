import sys
def main():

    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
        break

    nb = int(lines[0])
    for i in range(0, 4):
        if (nb % 3 == 0):
            nb /= 3
            continue
        if (nb % 2 == 0):
            nb /= 2
            continue
        if (nb % 2 != 0 and nb %3 != 0):
            nb -= 1
            continue
    print(int(nb))
    exit(0)

if __name__ == "__main__":
    main()