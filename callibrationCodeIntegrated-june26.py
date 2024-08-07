# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:36:44 2024

@author: zoech
"""

import os
import matplotlib.pyplot as plt
import numpy as np

''' file library '''

    # Old Calibration (load cell attached at one screw) (WEEK 1)
    # FORWARD TT "C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\jun26-forwardFunctionalDataSet.txt"
    
    # REVERSE TT "C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\jun27-reverseFunctionalDataSet.txt"
    
    # New Calibration (load cell attached at two screws) (WEEK 2)
    # FORWARD TT "C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\Jul1 Calibration two screws in L bracket positive cal factor.txt"
    
    # REVERSE TT "C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\Jul1 Calibration two screws in L bracket negative cal factor.txt"
    
    
''' reading input file '''

# Input file path
input_file_path =  r"C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\Callibration Code\Jul1 Calibration two screws in L bracket positive cal factor.txt"
output_file_path = 
readings = []
weights = []
ratios = []
 
# Read the data
with open(input_file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('Reading:'):
            reading = float(line.split(':')[1])
            readings.append(reading)
        elif line.startswith('Weight:'):
            weight = float(line.split(' ')[1])
            weights.append(weight)

for i in range(len(readings)):
    if weights[i] == 0:
        ratio = 0
    else:
        ratio = float(readings[i]/weights[i])
    ratios.append(round(ratio, 5))


''' writing to an output file '''

with open(output_file_path, 'x') as outfile:
    outfile.write("Reading\t     Weight (g)\t     Ratios\n")
   
    # Set number of rows
    max_rows = max(len(readings), len(weights),len(ratios))
   
    for i in range(max_rows):
        reading = readings[i] if i < len(readings) else ''
        weight = weights[i] if i < len(weights) else ''
        ratio = ratios[i] if i < len(ratios) else ''
        outfile.write(f"{reading}\t     {weight}\t     {ratio}\n"   )
    
    avg_ratio = sum(ratios)/(len(ratios)-1)
    outfile.write(f"\nAverage Ratio: {avg_ratio:.5f}\n")
 
print(f"Data has been written to {output_file_path}")
 

''' plotting '''

# Known Weight
x = weights

# TT Weight
y = readings
 
# Plotting the points
#plt.figure(figsize=(1,1))  # Adjust figure size
plt.plot(x, y, 'o', label='Data points')
 
# Fitting a linear regression line
coefficients = np.polyfit(x, y, 1)
poly = np.poly1d(coefficients)
y_fit = poly(x)
 
#P lotting the line of best fit
plt.plot(x, y_fit, label=f'Line of best fit: y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}', color='red')
 
# Calculating residuals and standard deviation
residuals = y - y_fit
std_dev = np.std(residuals)
 
# Calculating correlation coefficient (r)
correlation_matrix = np.corrcoef(x, y)
correlation_coefficient = correlation_matrix[0, 1]
 
# Adding standard deviation and correlation coefficient information to the plot
plt.text(0.95, 0.05, f'Standard Deviation: {std_dev:.2f}\nCorrelation Coefficient (r): {correlation_coefficient:.2f}\nCalibration Factor: {coefficients[0]:.2f}', 
         horizontalalignment='right', verticalalignment='bottom', transform=plt.gca().transAxes,
         bbox=dict(facecolor='yellow', alpha=0.5))

# Labeling axes and title
plt.xlabel('Known Weight (g)')
plt.ylabel('TT Weight')
plt.title('Known Weight vs. TT Weight with Line of Best Fit')
plt.legend()
 
# Showing the plot
plt.show()
 
 
