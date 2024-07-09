# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 1:55:49 2024

@author: zoech
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import re

#"C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\output change 1.txt"
#"C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\output change 3.txt"
# "C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\output change 4.txt"
# r"C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\output change 6 spring.txt"

# Input file path
input_file_path = r"C:\Users\zoech\Desktop\Jacks Reserach 2024\Code\HI Code\7-7-24 fabric 5.txt"

#sample = input("What are we measuring?: ")

# Initialize lists and variables
calibrated_ws = []
pulse_disps = []
disp = 0
decimal_pattern = r"-?\d+\.\d+"
int_pattern = r'-?\d+'
loops = []  # To store each loop data
current_loop = {'x': [], 'y': []}
previous_direction = None  # To track the previous direction

# Read input file
with open(input_file_path, 'r') as file:
    for line in file:
        line = line.strip()
        
        if "Calibration Factor" in line:
            cf = int(re.search(int_pattern, line).group())
            print("Calibration Factor:", cf)
            
        elif line.startswith('| step size:'):
            step_size = int(re.search(int_pattern, line).group())
            
            if "up" in line:
                direc = "up"
            else:
                direc = "down"

        elif line.startswith('| one reading:'):
            ws = re.findall(decimal_pattern, line)
            calibrated_ws.extend([float(w) for w in ws])
            
            if direc == "up":
                disp -= step_size
            else:
                disp += step_size
            
            pulse_disps.append(disp)
            current_loop['x'].append(disp)
            current_loop['y'].append(float(ws[0]))

            # Check if the direction changed from down to up, indicating the start of a new loop
            if previous_direction == "up" and direc == "down" and current_loop['x']:
                loops.append(current_loop)
                current_loop = {'x': [], 'y': []}

            previous_direction = direc

# Add the last loop if it's not empty
if current_loop['x']:
    loops.append(current_loop)

# Plot each loop with a different color
plt.figure(figsize=(10, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(loops)))

for i, loop in enumerate(loops):
    plt.plot(loop['x'], loop['y'], 'o-', label=f'Loop {i+1}', linewidth=1, markersize=2, color=colors[i])

# Add an arrow for "Up"
plt.annotate('Up', xy=(0.75, 0.3), xycoords='axes fraction',
             xytext=(0.9, 0.5), textcoords='axes fraction',
             arrowprops=dict(facecolor='green', shrink=0.05, width=1.5),
             horizontalalignment='right')

# Add an arrow for "Down"
plt.annotate('Down', xy=(0.25, 0.45), xycoords='axes fraction',
             xytext=(0.1, 0.3), textcoords='axes fraction',
             arrowprops=dict(facecolor='red', shrink=0.05, width=1.5),
             horizontalalignment='left')

# plt.text(0.9, 0.35, 'TT Weight increases ', horizontalalignment='right',
#           verticalalignment='bottom', transform=plt.gca().transAxes,
#           bbox=dict(facecolor='yellow', alpha=0.5))


# Labeling axes and title
plt.xlabel('Pulse Displacement')
plt.ylabel('TT Weight (g)')
plt.title('Pulse Displacement vs. TT Weight')
plt.legend()
plt.show()

#print(pulse_disps)
