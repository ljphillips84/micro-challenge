'''
HiPy Micro Challenge: "Splittsville"
Level: INTERMEDIATE
Pre-requisite: "read_data" (EASY)
Author: R. Treharne
Date: 21 Aug 2016
'''

import sys
import numpy as np

def read_to_col(fPath):
    '''
    read in large data file
    transpose data into columns and return as list of lists
    remember - first column is x data
    '''

    return

def split_data(data):
    '''
    reads in list of lists containing column data
    creates dictionary for x values - yields to generator
    creates dictionary for each column of y data,
    defines dict key as three digit integer filename
    (e.g. 001.csv) - yields each y dict to generator
    '''
    yield

def save_data(gen, dPath):
    '''
    reads in generator
    for each y dict in generator - x,y columns written to file 
    filename is key of y dict
    '''

if __name__ == "__main__":
    # arg1 - filename to be split
    # arg2 - save directory
    data = read_to_col(sys.argv[1])
    split = split_data(data)
    save_data(split, str(sys.argv[2]))

