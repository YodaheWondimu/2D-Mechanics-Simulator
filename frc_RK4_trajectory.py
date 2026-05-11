# Made by Yodahe Wondimu
# This project is under the MIT License, see LICENSE for more details.

# Demonstration: Trajectory Graphing with RK4 Integration and Air Resistance
# (An object, specifically FRC FUEL, tossed forward and upwards, facing Air Resistance and RK4 steppage along the way)
# Based on behaviors measured during FRC REBUILT in 2026

import numpy as np
import matplotlib.pyplot as plt

dt = 0.001   # timestep (seconds)

# lists of reached positions and their timestamps
xs = []
ys = []
times = []

t = 0.0

class Projectile:
    def __init__(self, mass, radius, Cd, rho=1.225):
        self.mass = mass                 # kg
        self.radius = radius             # meters
        self.Cd = Cd                     # drag coefficient
        self.rho = rho                   # air density (kg/m^3)
        self.area = np.pi * radius ** 2  # cross-sectional area (m^2)

## Adjust mass, radius, and drag coefficient as needed for different projectiles.
## In this case, we're going to model FUEL trajectories based on those in FRC Rebuilt.
fuel = Projectile(mass=0.215, radius=0.075, Cd=0.47)  # Example projectile properties

def derivatives(state, projectile=fuel):
    x, y, vx, vy = state

    v = np.array([vx, vy])
    speed = np.linalg.norm(v)

    # Forces
    gravity = np.array([0, -9.81 * projectile.mass])

    drag = np.array([0.0, 0.0])
    if speed > 0:
        drag_dir = -v / speed
        drag_mag = 0.5 * projectile.rho * projectile.Cd * projectile.area * speed ** 2
        drag = drag_dir * drag_mag

    force = gravity + drag
    accel = force / projectile.mass

    return np.array([vx, vy, accel[0], accel[1]])

def rk4_step(state, dt, projectile=fuel):
    k1 = derivatives(state, projectile)
    
    k2 = derivatives(state + 0.5 * dt * k1, projectile)
    
    k3 = derivatives(state + 0.5 * dt * k2, projectile)
    
    k4 = derivatives(state + dt * k3, projectile)

    return state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

state = np.array([0.0, 0.0, 2.644, 8.138])  # [x, y, vx, vy]
trajectory = []

while state[1] >= 0:
    xs.append(state[0])
    ys.append(state[1])
    times.append(t)

    state = rk4_step(state, dt, fuel)
    t += dt

plt.figure(figsize=(6, 4))
plt.plot(xs, ys, label="Projectile trajectory")
plt.xlabel("x position (m)")
plt.ylabel("y position (m)")
plt.title("2D Motion Under Gravity")
plt.legend()
plt.grid(True)
plt.show()