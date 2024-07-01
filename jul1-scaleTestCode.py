# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 13:25:31 2024

@author: zoech
"""
import os
import matplotlib.pyplot as plt
import numpy as np

# code for testing the TT as a scale

'''Opening Input File'''

input_file_path =  r"C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\weight accuracy test 2 (19.951g).txt"
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

# Setting Limits (makes it so it isn't scaled by default)
plt.xlim(0, 25)
plt.ylim(0, 110)

# Calculate Average
avg = sum(readings)/len(readings)

# Fitting a linear regression line
coefficients = np.polyfit(x, y, 1)
poly = np.poly1d(coefficients)
y_fit = poly(x)
 
#P lotting the line of best fit
plt.plot(x, y_fit, label=f'Line of best fit: y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}', color='red')
 
# Calculating residuals and standard deviation
residuals = y - y_fit
std_dev = np.std(residuals)
 
# Adding standard deviation and correlation coefficient information to the plot
plt.text(7, 80, f'Standard Deviation: {std_dev:.5f}', fontsize=12)
plt.text(7, 70, f'Average: {avg:.5f} g', fontsize=12)
plt.text(7, 60, f'True Weight: {"19.951 g"}', fontsize=12)

# Labeling axes and title
plt.xlabel('Reading Number')
plt.ylabel('Callibrated Weight (g)')
plt.title('Testing TT as a Scale')
plt.legend()
 
# Showing the plot
plt.show()

# print(readings)
# print(x)
# print(std_dev)
# print(correlation_coefficient)
# print(avg)
    
# PSUEDOCODE
# take input file and parse data into useful pieces
# need to have on the x axis the number of weights taken
# y axis is the tt reading

# from that we need to create a standard deviation and average (print both onto plot)
# idea == should create a flat line w slope 1
#     no output file needed? 
