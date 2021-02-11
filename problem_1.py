"""Problem 1 in Homework set 3 for ASTR260"""


import numpy as np

def f(x):
    """function to test in our derivative
    program"""
    return x**3 - 5*x + 2

def analytic_deriv_f(x):
    """The analytic derivative of
     x**3 - 5*x + 2."""
    return 3 * x**2 - 5

def absolute_error(truth, computed):
    """returns the absolute error between
    the computed and true value"""
    return np.abs(truth-computed)

def relative_error(truth, computed):
    """returns the relative error between
    the computed and true value"""
    numerator = absolute_error(truth, computed)
    denominator = np.abs(truth)
    return numerator/denominator

def forward_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the forward
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = f(x+h)-f(x)
    denominator = h
    return numerator/denominator
    
def deriv_forward_difference(h):
    '''computes the derivative of the forward difference method for error computation
    evaluated at x=0
    per the Mean Vlaue Theorem'''
    x=0
    numerator = forward_difference(x+h, h) - forward_difference(x, h)
    denominator = h
    return numerator/denominator

def central_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the central
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = f(x+h) - f(x-h)
    denominator = 2*h
    return numerator/denominator
    
def deriv_central_difference(h):
    '''computes the derivative of the central difference method for error computation
    evaluated at x=0'''
    x=0
    numerator = central_difference(x+h, h) - central_difference(x, h)
    denominator = h
    return numerator/denominator

if __name__ == "__main__":
    print("The central difference of x**3 - 5*x + 2,"+
          " evaluated at 0, with stepsize 0.01, is:")
    print(str(central_difference(0, 0.01, f))+'\n')

    print("Generating data for part 1 of problem 1.")
    #Data for part 1, over the range -5-->5
    output_data_fullrange = []
    h = 0.01
    #loop over an array from -5 to 5  in steps of 0.01
    for x_val in np.arange(-5, 5, h):
        #calculate analytic derivative, fw diff, and central diff
        analytic_diff = analytic_deriv_f(x_val)
        fw_diff = forward_difference(x_val, h, f)
        central_diff = central_difference(x_val, h, f)
        #store this as a tuple
        data = (x_val, analytic_diff, \
                fw_diff, central_diff)
        #append this to a list
        output_data_fullrange.append(data)

    #save this as an output textfile for plotting
    fname_part1 = 'problem_1_1_data.txt'
    np.savetxt(fname_part1, #filename
               np.array(output_data_fullrange), #data to save
               delimiter=',', #how to separate values in the file
               header=("function: x**3-5x+3\n"+
               "x, analytic_deriv(x), fw_diff(x), central_diff(x)"),
               fmt = '%.05f')#<--5 digits of precision, look up "format codes"
    print("Saved part 1 data to: "+fname_part1+'\n')
   
    print('Generating data for part 2: ')
    error_output_data_fullrange = []
    for h in np.arange(0.00001, .1, .00001):
        fw_diff_error = deriv_forward_difference(h) * h/2
        cntl_diff_error = deriv_central_difference(h) * h/2
        
        #store data as a tuple
        error_data = (h, fw_diff_error, cntl_diff_error)
        #append this to a list
        error_output_data_fullrange.append(error_data)
        
    #Save data for part 2
    fname_part2 = 'problem_1_2_data.txt'
    np.savetxt(fname_part2, #file name
               np.array(error_output_data_fullrange), #data to save
               delimiter=',', 
               header='h, fw_diff_error, cntl_diff_error',
               fmt='%.05f')
    print('Saved part 2 data to: '+fname_part2+'\n\n')