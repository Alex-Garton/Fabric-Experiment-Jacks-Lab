# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:51:49 2024

@author: zoech
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import re

### files
#"C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\fakie_data_;).txt"
#"C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\output change 1.txt"
#"C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\output change 3.txt"
# "C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\output change 4.txt"
# "C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\output change 5 spring.txt"
#"C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\output change 6 spring.txt"

''' Getting info from the input file '''

# Input file path
input_file_path =  r"C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\output change 6 spring.txt"
# Output file path
output_file_path = r"C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\HI-try1"

calibrated_ws = []
pulse_disps = []
disp = 0
decimal_pattern = r"-?\d+\.\d+"
int_pattern = pattern = r'-?\d+'


with open(input_file_path, 'r') as file:
    for line in file:
        line = line.strip()
        
        if "Calibration Factor" in line:
            cf = int(re.search(int_pattern, line).group())
            print(cf)
            
        elif line.startswith('| step size:'):
            step_size = int(re.search(int_pattern, line).group())
            
            # print(step_size)
            # print("hi")
            
            if "up" in line:
                direc = "up"
            else:
                direc = "down"

        elif line.startswith('| one reading:'):
            ws = re.findall(decimal_pattern, line)
            calibrated_ws.extend([float(w) for w in ws])
            
            # print(direc)
            
            if direc == "up":
                disp+= step_size
            else:
                disp-= step_size
            
            pulse_disps.append(disp)
            
print(calibrated_ws)
#print(pulse_disps)

''' Graphing ''' 
x = pulse_disps
y = calibrated_ws
 
# Plotting the points
plt.ylim(-120,10)
plt.plot(x, y, 'o', label='Data points', linestyle='-')

# Labeling axes and title
plt.xlabel('Pulse Displacement')
plt.ylabel('TT Weight')
plt.title('Pulse Displacement vs. TT Weight')
#plt.text(200, -100, f'Calibration Factor: {cf:.2f}', fontsize=12, color='red')

#plt.legend()
 
plt.show()
 
 
