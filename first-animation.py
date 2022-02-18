from math import dist
from timeit import repeat
from turtle import update
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation   
import numpy as np

###################### Calculation Part ######################

# Setting up the duration of animation
start_t = 0
end_t = 2
delta_t = 0.005

# Array of time
t = np.arange(start_t, end_t + delta_t, delta_t)

# Array of distance
distance = 800 * t

# Array of altitude
altitude = np.ones(len(t)) * 2

###################### Animation Part ######################

frame_amt = len(t)

# Setup figure 
fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(2, 2)

ax0 = fig.add_subplot(gs[0, :], facecolor=(0.9, 0.9, 0.9))

line, = ax0.plot([], [], 'b', linewidth=2)

# Define animation function
def update_plot(num):
    line.set_data(distance[0:num], altitude[0:num])
    
    return line, 

# Animation
ani = animation.FuncAnimation(fig, update_plot, frames=frame_amt, interval=20, repeat=True, blit=True)

# Plot setup for axis
plt.xlim(distance[0], distance[-1])
plt.ylim(0, altitude[0] + 1)

plt.show()