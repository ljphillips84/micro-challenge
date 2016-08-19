import numpy as np
import sys

def deg_to_rad(deg):
    
    return '{0:.1f} deg = {1:.1f} rad'.format(float(deg),(float(deg)*np.pi))

if __name__ == "__main__":
    print(deg_to_rad(sys.argv[1]))
