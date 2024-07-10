# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 13:25:31 2024

@author: zoech
"""
import os
import matplotlib.pyplot as plt
import numpy as np

true_w = input("Please enter the scale-measured weight of the object: ")

# code for testing the TT as a scale

'''Opening Input File'''

input_file_path =  
readings = []
 
# Read the data
with open(input_file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('Reading:'):
            reading = float(line.split(' ')[1])
            readings.append(reading)
        
       
'''Creating Plot'''

# Reading Number
x = [i for i in range(1, len(readings) + 1)]

# Calculated Weight (using Callibration Factor)
y = readings
 
# Plotting the points
plt.plot(x, y, 'o', label='Data points')

# Calculate Average
avg = sum(readings)/len(readings)

# Setting y-axis
plt.ylim(0, 2*avg)

# Fitting a linear regression line
coefficients = np.polyfit(x, y, 1)
poly = np.poly1d(coefficients)
y_fit = poly(x)
 
#P lotting the line of best fit
plt.plot(x, y_fit, label=f'Line of best fit: y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}', color='red')
 
# Calculating residuals and standard deviation
residuals = y - y_fit
std_dev = np.std(residuals)
 
plt.text(0.95, 0.2, f'Standard Deviation: {std_dev:.5f}\nAverage: {avg:.5f} g\nTrue Weight: {true_w}', 
         horizontalalignment='right', verticalalignment='bottom', transform=plt.gca().transAxes,
         fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))

# Labeling axes and title
plt.xlabel('Reading Number')
plt.ylabel('Callibrated Weight (g)')
plt.title('Testing TT as a Scale')
plt.legend()
 
# Showing the plot
plt.show()

    
