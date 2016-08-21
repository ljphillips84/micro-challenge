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

def plot_file(fPath, xlabel='', ylabel='', sPath=None):
    '''
    Plots data  comma separated .txt or .csv file
    Uses solution to read_data challenge to read/format data
    fPath - path to data file
    xlabel - string label for x-axis
    ylabel - string label for y-axis
    sPath - path to save output .png file
    '''

