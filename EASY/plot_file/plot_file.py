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
    Plots a comma separated .txt or .csv file
    Uses solution to read_data challenge to read/format data
    extra parameters available for x/y labels
    '''


