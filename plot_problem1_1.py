import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    fname_part1 = 'problem_1_1_data.txt'
    derivative_data = np.loadtxt(fname_part1,
                              delimiter=',')
    
    #store data into convienent graphing variables
    x_val = derivative_data[:,0]
    analytic_deriv = derivative_data[:,1]
    fw_diff = derivative_data[:,2]
    cntl_diff = derivative_data[:,3]
    
    #plot the data
    plt.title("Forward and Cnt'l Difference Method Overlay")
    plt.plot(x_val, analytic_deriv, color='black')
    plt.plot(x_val, fw_diff, color='cyan')
    plt.plot(x_val, cntl_diff, color='magenta')
    
    plt.show()