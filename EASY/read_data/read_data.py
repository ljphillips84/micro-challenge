'''
HiPy Micro Challenge: "Read Data"
Level: EASY 
Pre-requisite: None
Author: R. Treharne
Date: 21 Aug 2016
'''

import sys
import numpy as np

def read_to_row(fPath):
    '''
    read all lines in data file
    return a list of lists containing row data
    '''

    data = [] # define empty list

    # open file to read
    with open(fPath, "r") as f:
        for line in f.readlines(): # read every line and then loop through
            # split each line into list using comma 
            # loop through each element in new list and make float
            # append item to data list
            data.append([float(x) for x in line.split(",")])

    return data # return the list

def read_to_col(fPath):
    '''
    return transposed data as a list of lists containing column data
    '''
    return np.transpose(read_to_row(fPath)) # just transpose the rows

if __name__ == "__main__":
    print(read_to_row(sys.argv[1]))

