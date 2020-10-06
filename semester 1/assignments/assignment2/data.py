#################
# Mandatory Assignment 2 - IDSP
#################

# Assignment: 	Working with Files
# Author: 		Jonas-Mika Senghaas
# Date: 		16. September 2020
# TA:			Simon Martin Breum

import os

def read_file(filename):
    L = []
    infile = open(filename, "r")

    for line in infile:
        L.append(line.strip())

    return L


def parse_csv_lines(lines):
    L = []

    for line in lines:
        L.append(line.split(","))

    return L


def parse_delimited_lines(lines, delimiter):
    L = []

    for line in lines:
        L.append(line.split(str(delimiter)))

    return L


def age_difference(lines):
    L = []

    for line in lines:
        age_difference = float(line[-1]) - float(line[1])
        L.append(round(age_difference, 2))

    return L


def find_unisex_names(male_names, female_names):
    unisex_names = set()

    for name in male_names:
        if name in female_names:
            unisex_names.add(name[0])

    return unisex_names


def build_name_dataset(female_names, male_names, unisex_names):
    outfile = open("all_names.csv", "w")
    unique = set()

    for name in female_names:
        if name[0] in unisex_names:
            gender = "U"
        else:
            gender = "F"
        unique.add("{0}, {1}".format(name[0], gender))

    for name in male_names:
        if name[0] in unisex_names:
            gender = "U"
        else:
            gender = "M"
        unique.add("{0}, {1}".format(name[0], gender))

    for name in unique:
        outfile.write(name + "\n")

    print("Done")
    return None


def write_sorted_names(names):
    import os
    import shutil as st

    try:
        st.rmtree("data")
    except:
        None

    os.mkdir("data")

    for name in names:
        first = name[0][0].upper()
        f = open("data/{0}.csv".format(first), "a")
        f.write("{0}\n".format(name[0]))
        f.close()

    print("Done")
    return None


def main():
    file1 = "male_names.csv"
    file2 = "female_names.csv"
    file3 = "municipalities-2005-2019.csv"

    path_male = os.path.join(os.path.dirname(__file__), file1)
    path_female = os.path.join(os.path.dirname(__file__), file2)
    path_muni = os.path.join(os.path.dirname(__file__), file3)

    # print(os.path.dirname(__file__))
    # print(path_male)

    lines_male = read_file(path_male)
    lines_female = read_file(path_female)
    lines_muni = read_file(path_muni)
    #print(lines_male)
    # print(lines_female)
    # print(lines_muni)

    ##########
    parsed_lines_male = parse_csv_lines(lines_male)
    parsed_lines_female = parse_csv_lines(lines_female)
    parsed_lines_muni = parse_csv_lines(lines_muni)
    # print(parsed_lines_male)
    # print(parsed_lines_female)
    # print(parsed_lines_muni)

    ##########
    dparsed_lines_male = parse_delimited_lines(lines_male, ";")
    dparsed_lines_female = parse_delimited_lines(lines_female, ";")
    dparsed_lines_muni = parse_delimited_lines(lines_muni, ";")
    # print(dparsed_lines_male)
    # print(dparsed_lines_female)
    # print(dparsed_lines_muni)

    ##########
    age_difference_muni = age_difference(dparsed_lines_muni)
    # print(age_difference_muni)

    ##########
    unisex_names = find_unisex_names(parsed_lines_male, parsed_lines_female)
    # print(unisex_names)

    ##########
    # Creates CSV-File "all_names.csv" in current directory

    if input("Do you want to create 'all_names.csv'?: ").upper() == "Y":
        build_name_dataset(parsed_lines_female,
                           parsed_lines_male, unisex_names)
    else:
        print("\n --- The file was not created")

    path_all_names = "/Users/jonassenghaas/python/itu/08/assignment2/all_names.csv"

    # n
    # Creates 32 CSV-Files in new directory "data" within the current directory
    # open and parse "all_names.csv" file to use it in next funtion
    allnames = parse_csv_lines(read_file(path_all_names))
    if input("Do you want to create 32 files with names? (Y/N): ").upper() == "Y":
        write_sorted_names(allnames)
    else:
        print("\n --- The files were not created")


if __name__ == "__main__":
    main()
