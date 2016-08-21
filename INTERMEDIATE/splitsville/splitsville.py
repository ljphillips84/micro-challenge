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
    data = [] # define empty data list

    with open(fPath, 'r') as f: # open file loop
        for line in f.readlines():
            # split line on ","
            # convert all vaules in split list to float
            # add to data list.
            data.append([float(x) for x in line.split(",")])

    return np.transpose(data) # don't forget to transpose

def split_data(data):
    '''
    reads in list of lists containing column data
    creates dictionary for x values - add to generator
    creates dictionary for each column of y data,
    defines dict key as three digit integer filename
    (e.g. 001.csv) - add to genrator
    '''
    yield {"x": data[0]} # give up x dictionary to generator
    for idx, lst in enumerate(data[1:]): # loop through rest of lists and keep increment through index idx
        yield {"{0}.csv".format(str(idx+1).zfill(3)): lst}

def save_data(gen, dPath):
    '''
    reads in generator
    for each y dict in generator - x,y columns written to file 
    filename is key of y dict
    '''
    x = next(gen).get("x", None)
    for item in gen:
        fPath = next(iter(item))
        y = item.get(fPath, None)
        with open("{0}/{1}".format(dPath, fPath), "w") as f:
            for i,j  in zip(x,y):
                f.write("{0},{1}\n".format(i, j))

if __name__ == "__main__":
    data = read_to_col(sys.argv[1])
    split = split_data(data)
    save_data(split, str(sys.argv[2]))

