#2D DIFFUSION SIMULATION THROUGH RANDOM WALK

import numpy as np
import matplotlib.pyplot as plt
import random
import seaborn as sns
    
N = 1000000
Dx = Dy = 1
Dt = 1
t_max = 100
t = 0
x = np.zeros(N)
y = np.zeros(N)
grid_size = 1000  # Number of points in each dimension
x_range = np.linspace(-25, 25, grid_size)
y_range = np.linspace(-25, 25, grid_size)
X, Y = np.meshgrid(x_range, y_range)

NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4; STAY = 5;  # constants
while t < t_max:
    movements = np.random.randint(1,6,N)
    y += np.where(movements==NORTH,1,0)
    y -= np.where(movements==SOUTH,1,0)
    x += np.where(movements==EAST,1,0)
    x -= np.where(movements==WEST,1,0)
    t += Dt

x_average = np.average(x)
y_average = np.average(y)
d = np.sqrt(np.average(x**2) + np.average(y**2)) #average displacement
D = (Dx**2)/5*Dt #diffusion_coefficent
distance =  np.sqrt(4*t*D)        
Z = np.exp(-(X ** 2 + Y ** 2) / (4 * D * t)) #analytical solution of diffusion equation
Z /= (4 * np.pi * D * t) #normalization
fig, ax1 = plt.subplots(figsize=(10,10))
sns.histplot(x=x, y=y, discrete=[True, True], stat='count', ax=ax1, thresh=50)
ax1.scatter(x_average, y_average, c='black', label='average position')
ax1.add_patch(plt.Circle((0,0), d, label = "avg distance", color='red', fill=False))
ax1.set_xlim(-25,25)
ax1.set_ylim(-25,25)
ax1.set_title(f"Simulation: <(x,y)> = {(round(x_average, 5), round(y_average, 5))}; avg_distance = {round(d, 5)}")
ax1.legend()
# Analytical Solution Plot
#heatmap = ax2.imshow(Z, extent=(-25, 25, -25, 25), origin='lower', cmap='Blues')
#ax2.add_patch(plt.Circle((0,0), distance, label = "distance", color='red', fill=False))
#ax2.set_xlim(-25, 25)
#ax2.set_ylim(-25, 25)
#ax2.legend()
#ax2.set_title(f"Analytical Solution: distance = {round(distance,5)}")
fig.suptitle(f"Diffusion of {N} particles after {t} iterations\nDistance error = {round((np.abs(d-distance)/d)*100,2)} %")
plt.savefig(f"output/SimulationN={N}.png")
plt.show()