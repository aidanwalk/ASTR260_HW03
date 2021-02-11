"""Problem 2 from Hwk 3 of ASTR260"""
import math
import numpy as np

def x(t):
    return math.sin(2*math.pi*0.02*100*t)

def analytic_velocity(t):
    '''returns Analytical derivative of X(t)= 1*sin(2*pi*(0.02*100)*t)'''
    return (2*math.pi*0.02*100) * math.cos(2*math.pi*0.02*100*t)

def forward_difference_velocity(position, next_position, h):
    '''  COMMENT   '''
    numerator = next_position - position
    denominator = h
    return numerator/denominator
    
def central_difference_method(previous_position, next_position, h):
    '''COMMENT'''
    numerator = next_position - previous_position
    denominator = h
    return numerator/denominator

if __name__ == "__main__":
    analytic_data = []
    #calculate the theoretical, analytical derivative
    for t in np.arange(0, 100, 0.01):
        analytic_v = analytic_velocity(t)
        analytic_data.append(analytic_v)

    #load data from .txt file
    path_to_data = "/Users/aidan/Desktop/School/Coding/Python/260/HW03/sensor_position_data.txt"
    oscillator_data = np.loadtxt(path_to_data, skiprows=1, delimiter=',')
    #pulls out the first column (remember things start at 0 in python)
    oscillator_time = oscillator_data[:,0]
    oscillator_pos  = oscillator_data[:,1]

    derivative_data = []
    for x in range(1, len(oscillator_time)-1):
        #find step size
        h = oscillator_time[x+1] - oscillator_time[x]
        #find current, previous, and post positions of the system
        position = oscillator_pos[x]
        previous_position = oscillator_data[x-1]
        next_position = oscillator_pos[x+1]
        #find the current time
        current_time = oscillator_time[x]
        
        #calculate the forward and central differences
        fw_diff = forward_difference_velocity(position, next_position, h)
        cntl_diff = central_difference_method(previous_position, next_position, h)
        
        #save data to a tuple
        data = (current_time, fw_diff, cntl_diff)
        #append to a list
        derivative_data.append(data)
    
    #save data
    fname = 'problem_2_data.txt'
    np.savetxt(fname, #filename
               np.array(derivative_data), #data to save
               delimiter=',')
               
    print("Saved data to: "+fname+'\n')