########## 
# Tryout - This is a file to learn to work with the external libraries Numpy and Matplotlib, that are used to analyse large data sets
##########

# Author		: 	Jonas-Mika Senghaas
# Date Created	:	14.09.2020

import os
import numpy as np
import matplotlib.pyplot as plt
import csv


# we are working with a csv dataset of the stockholm temperature data, so we want to load it
def load_data(infile):
    # this loads the stockholm data into a numpy array
    return np.loadtxt(infile)

# to get an overview over the data, we can find slice the data set to all the years measured and give the range and total amount of measured years


def get_year_info(data):
    years_measured = np.unique(data[:, 0])

    # print(years_measured)
    # print("Years measured from {} to {}\nNumber of years measured in total: {}".format(int(years_measured[0]), int(years_measured[-1]) , len(years_measured)))

# now i wanna get an overview over the actual development of the temperature over the years, which can be found in the last column at index -1 (or 3


def get_temp_info(data):
    temperature = data[:, -1]

    # print(temperature.shape) # here we have again created a test case to see, that we have sliced the last column correclty
    # print(np.ndim(temperature)) # it obviously has the dimension 1

    # print(temperature.max())
    # print(temperature.min())
    # print(np.average(temperature))
    # print(np.median(temperature))

# lets try to plot our temperature data, first for one specific year, and then for every data element


def average_temp_year(year: int, data):
    mask = data[:, 0] == year
    temperature_year = data[mask]

    months = np.unique(temperature_year[:, 1])
    # print(months)

    average_temp = []

    for i in range(12):
        view = temperature_year[:, 1] == float(i+1)
        month = temperature_year[view]
        average_temp.append(round(np.average(month[:, -1]), 2))

    arr = np.array([months, average_temp])

    return arr


def plotting_average_temp(average_temp_per_month):
    months = average_temp_per_month[0]
    print(months)
    average_temp = average_temp_per_month[1]

    f = plt.figure(figsize=(16, 9))
    axes = f.add_axes([0.1, 0.1, 0.8, 0.8])

    axes.bar(months, average_temp)

    axes.set_xlabel('Months')
    axes.set_ylabel('Average Temperature (°C)')
    axes.set_title('Average Temperature in 1800 in Stockholm')

    axes.set_xticks(months)
    #axes.set_xticklabels("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "Novemeber", "December");
    plt.xticks(rotation='vertical')

    f.savefig("average_temp_1800.pdf")


def main():
    # first we need to specify the path, where the file is located and from where it should be loaded
    infile_name = "lecture12_lecturematerial/stockholm_temperatures.dat"
    infile = os.path.join(os.path.dirname(__file__), infile_name)

    stockholm_data = load_data(infile)

    ############
    # print(stockholm_data.shape) # test for array shape > outputs (77431,4), so 77431 rows and 4 columns
    # print(np.ndim(stockholm_data)) # test which dimnesion the array has, which is two (table)
    ############

    average_temp_1800 = average_temp_year(1800, stockholm_data)
    # print(average_temp_1800)

    plotting_average_temp(average_temp_1800)

if __name__ == "__main__":
    print("Everything is working!")
    main()
