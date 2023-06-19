# 2D Diffusion Simulation through Random Walk

This repository contains a Python code for simulating 2D diffusion through a random walk. The code compares the simulation results with the analytical solution of the diffusion equation.

![DiffusionSimulation](https://github.com/alessandroAbati/2DRandomWalkSimulation/assets/136715422/0506bd82-6c41-49a4-aa23-7ef5cc6cdf93)

## Random Walk
In this simulation, particles undergo a random walk in a 2D space. The position of each particle is updated at each time step based on a random direction chosen from the set of north, south, east, west, and stay. The number of particles, step sizes, time step, and stopping time can be configured in the code.

## Analytical Solution of Diffusion Equation
The simulation results are compared with the analytical solution of the diffusion equation. The code initializes a grid of points and calculates the analytical solution at each point. The analytical solution represents the expected distribution of particles over time according to the diffusion equation.

## Dependencies
The following dependencies are required to run the code:
- numpy
- matplotlib
- random
- seaborn

## Usage
1. Clone the repository or download the code file.
2. Make sure you have the required dependencies installed.
3. Open the code file and adjust the parameters such as the number of particles, step sizes, time step, and stopping time as desired.
4. Run the code and observe the simulation results.

## Simulation Results
The code generates two plots for each iteration. The first plot shows the simulation results, including the position of particles, the average position, and the average distance traveled by the particles. The second plot displays the analytical solution of the diffusion equation, representing the expected distribution of particles over time. Both plots are displayed side by side for visual comparison.

The code also calculates the average displacement of particles and the analytical displacement at the end of the simulation. The percentage error between these two values is calculated and displayed in the title of the second plot.

Please note that the code saves the plots in a directory named "output". You can uncomment the line `#plt.savefig(f"output/Simulation{t}.png")` to save the plots as image files.

Feel free to experiment with different parameters and analyze the behavior of diffusion through a random walk.

Moreover, studying the behavior of the error between the average displacement and the analytical displacement with respect to the number of particles simulated (N), we can notice that:

1. As the number of particles (N) increases, the error between the average displacement and the analytical displacement tends to decrease. This is because a larger number of particles provides a more accurate representation of the overall particle distribution.

2. With a small number of particles, the random walk simulation may not fully capture the characteristics of diffusion. The distribution of particles may exhibit higher variability, leading to larger errors compared to the analytical solution.

3. As the number of particles increases, the random walk simulation converges towards the analytical solution. The average displacement becomes more representative of the expected behavior, resulting in a smaller error.

4. It's important to note that the convergence rate may depend on other factors such as the step sizes, time step, and the characteristics of the diffusion process being simulated. However, in general, increasing the number of particles improves the accuracy of the simulation and reduces the error.

![2DRandomWalkChangingN](https://github.com/alessandroAbati/2DRandomWalkSimulation/assets/136715422/c92a2627-9e2f-48a6-9665-39de6a03e478)

To study the behavior of the error in more detail, you can perform experiments by varying the number of particles (N) and observe how the error changes. By plotting the error against N, you can analyze the trend and determine the optimal number of particles required to achieve a desired level of accuracy in the simulation.

**Note:** This code was written for educational purposes to demonstrate the concept of 2D diffusion simulation and its comparison with the analytical solution. It may not be optimized for large-scale simulations or production environments.
