#!/usr/bin/env python3
import sys

def get_characters():
    array1 = []
    array2 = []
    i = 0
    for line in sys.stdin:
        if len(array1) == 0:
            array1 = line
        else :
            array2 = line
        i += 1
        if i == 2:
            break
    array1.strip('\n')
    array2.strip('\n')
    return array1, array2

def compare(array1, array2):
    similarity = []
    for char in array1:
        for other_char in array2:
            if (char == other_char):
                similarity.append(char)
    return similarity

def check_order(array2, similarity):
    order = []
    for char in similarity:
        for i in range(len(array2)):
            if char == array2[i]:
                order.append(i)
                break
    if (len(order) <= 2):
        return False
    for i in range(len(order) - 1):
        if order[i] > order[i + 1]:
            return False
    print(similarity)
    print(order)
    return True

if __name__ == "__main__":
    try:
        array1, array2 = get_characters()
        similarity = compare(array1, array2)
        if check_order(array2, similarity) == True:
            print("TEMPEST")
        else :
            print("NORMAL")

    except:
        exit(84)