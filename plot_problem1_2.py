import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
        fname_part2 = 'problem_1_2_data.txt'
        error_data = np.loadtxt(fname_part2,
                            delimiter=',')

        #save data into convinient graphing variables
        h = error_data[:,0]
        fw_error = error_data[:,1]
        cntl_error = error_data[:,2]
    
        #plot data
        plt.title("Forward and Cnt'l Difference Method Error Evaluated at x=0")
        plt.xlabel("Step Size (h)")
        plt.ylabel("Local Truncation Error")
        plt.plot(h, fw_error, color='red')
        plt.plot(h, cntl_error, color='black')
        
        plt.show()
    
    
    