from curses.ascii import alt
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

# Draw airplane
plane_1, = ax0.plot([], [], 'k', linewidth=10)
wing_1, = ax0.plot([], [], 'k', linewidth=5)
wing_2, = ax0.plot([], [], 'k', linewidth=5)
tail_1, = ax0.plot([], [], 'k', linewidth=3)
tail_2, = ax0.plot([], [], 'k', linewidth=3)


# Draw houses
house1 = ax0.plot([100, 100], [0, 1.0], 'k', linewidth=7)
house2 = ax0.plot([300, 300], [0, 1.0], 'k', linewidth=7)
house3 = ax0.plot([700, 700], [0, 0.7], 'k', linewidth=15)
house4 = ax0.plot([900, 900], [0, 0.9], 'k', linewidth=10)
house5 = ax0.plot([1300, 1300], [0, 1.0], 'k', linewidth=20)

# Define animation function
def update_plot(num):
    line.set_data(distance[0:num], altitude[0:num])
    
    plane_1.set_data([distance[num] - 40, distance[num] + 20], 
                        [altitude[num], altitude[num]])  

    wing_1.set_data([distance[num] - 20, distance[num]], 
                        [altitude[num] + 0.3, altitude[num]]) 

    wing_2.set_data([distance[num] - 20, distance[num]], 
                        [altitude[num] - 0.3, altitude[num]]) 

    tail_1.set_data([distance[num] - 40, distance[num] - 30], 
                        [altitude[num] + 0.15, altitude[num]]) 
    
    tail_2.set_data([distance[num] - 40, distance[num] - 30], 
                        [altitude[num] - 0.15, altitude[num]]) 
    
    return line, plane_1, wing_1, wing_2, tail_1, tail_2

# Animation
ani = animation.FuncAnimation(fig, update_plot, frames=frame_amt, interval=20, repeat=True, blit=True)

# Plot setup for axis
plt.xlim(distance[0], distance[-1])
plt.ylim(0, altitude[0] + 1)

plt.xticks(np.arange(distance[0], distance[-1] + 1, distance[-1] / 4), size=15)
plt.yticks(np.arange(0, altitude[-1] + 2, altitude[-1] / altitude[-1]), size=15)
plt.xlabel("Distance", fontsize=15)
plt.ylabel("Altitude", fontsize=15)
plt.title("Airplane")
plt.grid(True)
plt.show()