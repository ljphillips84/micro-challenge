'''
HiPy Micro Challenge: "Plot File"
Level: EASY 
Pre-requisite: "read_data.py"
Author: R. Treharne
Date: 21 Aug 2016
'''

import sys
import numpy as np
from read_data import *
import matplotlib.pyplot as plt

def plot_file(fPath, xlabel='', ylabel=''):
    '''
    Plot a comma separated .txt or .csv file
    Use solution to read_data challenge to read/format data
    '''
    fig = plt.figure() # define figue object
    ax = fig.add_subplot(111) # add axis
    d = read_to_col(fPath) # get data in columns
    ax.plot(d[0], d[1], '-') # plot the data
    # set axis labels
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show() # don't forgot to show the plot

if __name__ == "__main__":
    try:
        xlabel = sys.argv[2]
    except:
        xlabel = ''
    try:
        ylabel = sys.argv[3]
    except:
        ylabel = ''

    plot_file(sys.argv[1], xlabel, ylabel)

