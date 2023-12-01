#!/usr/bin/env python3
import sys

def get_numbers():
    array = []
    array_zebi = []
    int_array = []
    i = 0
    for line in sys.stdin:
        if len(array) == 0:
            array = line
        break
    array.strip('\n')
    array_zebi = array.split()
    for number in array_zebi:
        int_array.append(int(number))
    return int_array

def get_apparitions(array, dict):
    do_break = 0
    for number in array:
        do_break = 0
        for key in dict.keys():
            if (key == number):
                dict[key] += 1
                do_break = 1
        if (do_break == 1):
            continue
        dict[number] = 1
    return dict

def get_max(dict):
    max = []
    max_occurence = 0
    has_break = 0
    for key in dict.keys():
        if dict[key] > max_occurence:
            max = list()
            max.append(key)
            max_occurence = dict[key]
        if dict[key] == max_occurence:
            for number in max:
                if number == key:
                    has_break = 1
            if (has_break == 0):
                max.append(key)
            has_break = 0
    return max

def get_min(dict):
    min = []
    min_occurence = 10000
    has_break = 0
    for key in dict.keys():
        if dict[key] < min_occurence:
            min = list()
            min.append(key)
            min_occurence = dict[key]
        if dict[key] == min_occurence:
            for number in min:
                if number == key:
                    has_break = 1
            if (has_break == 0):
                min.append(key)
            has_break = 0
    return min

if __name__ == "__main__":
    array = []
    dict = {}
    maxi = []
    max_number = 0
    mini = []
    min_number = 0
    try:
        array = get_numbers()
        dict = get_apparitions(array, dict)
        maxi = get_max(dict)
        mini = get_min(dict)
        max_number = max(maxi)
        min_number = min(mini)
        print(max_number - min_number)
    except:
        exit(84)