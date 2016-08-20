import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def rosen(x, y, a=1, b=100):
    '''
    Input x and y values and return value for Rosenbrock function
    '''
    f = (a - x)**2 + b*(y-x**2)**2
    return f

def plot3D(x, y, func):
    '''
    Input 2D function and generate a 3D surface plot
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(x, y)
    z = []
    for x, y in zip(X.ravel(), Y.ravel()):
        z.append(rosen(x, y))
    Z = griddata(X.ravel(), Y.ravel(), z, X, Y, interp="linear")
    ax.plot_surface(X, Y, Z, cmap = cm.jet)
    plt.show()
    
    #ax.plot_surface(X, Y, Z)
    #plt.show()



if __name__ == "__main__":
    x = y = np.linspace(-1, 1, 100)
    plot3D(x, y, rosen)
    

    


