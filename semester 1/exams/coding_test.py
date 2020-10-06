##########
# Coding Test
##########

# Author		: 	Jonas-Mika Senghaas
# Date Created	:	05.10.2020

import collections


def read_csv(filename):
    dict = {}

    with open(filename, "r") as infile:
        i = 1

        headers = [header for header in infile.readline().strip().split(",")]
        for header in headers:
            dict[header] = []

        for line in infile.readlines():
            i = 0
            for item in line.strip().split(","):
                dict[headers[i]].append(item)
                i += 1

    return dict


def compute_mode(integer_list):
    mode_list = []
    counter_dict = collections.Counter(integer_list)
    most_common = 0

    # find most common
    for count in counter_dict:
        if counter_dict[count] > most_common:
            most_common = counter_dict[count]

    # append all numbers with this number of occureneces to the return list
    for item in counter_dict:
        if counter_dict[item] == most_common:
            mode_list.append(item)

    return sorted(mode_list)  # sort the list


def main():
    test_read = read_csv("test.txt")
    # print(test_read)

    test_list = [-99, 45, 8, 45, 8, 5, 6, 6]

    test_mode = compute_mode(test_list)
    print(test_mode)


if __name__ == "__main__":
    print("Coding Test Results are running...")
    main()
