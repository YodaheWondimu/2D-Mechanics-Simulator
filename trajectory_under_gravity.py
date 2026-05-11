# Made by Yodahe Wondimu
# This project is under the MIT License, see LICENSE for more details.

# Demonstration: Trajectory graphing
# (An object tossed forward and upwards, hits multiple position points on its way up and down)
# Based on behaviors measured during FRC REBUILT in 2026

import numpy as np
import matplotlib.pyplot as plt

g = 9.81    # gravity (m/s^2)
dt = 0.001   # timestep (seconds)
t_max = 5.0 # total simulation time (seconds)

x = 0.0 # initial x position (m)
y = 0.0 # initial y position (m)

vx = 2.644   # initial x velocity (m/s)
vy = 8.138   # initial y velocity (m/s)

# lists of reached positions and their timestamps
xs = []
ys = []
times = []

t = 0.0

# object tossed up and to the right + restitution
# pendelum next time?
while t <= t_max:
    # Record current state
    xs.append(x)
    ys.append(y)
    times.append(t)

    # Accelerations
    ax = 0.0
    ay = -g

    # Update velocity (Euler)
    vx += ax * dt
    vy += ay * dt

    # Update position (Euler)
    x += vx * dt
    y += vy * dt

    if (y < 0):
        break
    
    # restitution: can be used to model bouncing but wasn't necessary for this demonstration
    # if y < 0:
    #     y = 0
    #     vy = -0.8 * vy   

    t += dt

plt.figure(figsize=(6, 4))
plt.plot(xs, ys, label="Projectile trajectory")
plt.xlabel("x position (m)")
plt.ylabel("y position (m)")
plt.title("2D Motion Under Gravity")
plt.legend()
plt.grid(True)
plt.show()