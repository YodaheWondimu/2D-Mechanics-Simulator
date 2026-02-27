# Made by Yodahe Wondimu
# This project is under the MIT License, see LICENSE for more details.

# Demonstration: Shooter velocity lookup table generator / FRC Lookup Table
# Computes required initial velocity (v0) at fixed launch angle
# to hit a target of known height at various horizontal distances.
# Based on behaviors measured during FRC REBUILT in 2026

import numpy as np
import matplotlib.pyplot as plt
import csv

def simulate_projectile(v0, theta, target_height, dt=0.001):
    g = 9.81

    x, y = 0.0, 0.0
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)
    previous_y = y

    while y >= 0:
        
        # Check if we passed target height
        if (previous_y - target_height) * (y - target_height) <= 0 and vy < 0:
            return x

        previous_y = y
        vy -= g * dt
        x += vx * dt
        y += vy * dt

    return None

# Now, take your found values from the filled array and convert it into a .csv file
theta = np.radians(45)
target_height = 1.134  # meters

velocities = np.linspace(1, 25, 500)

lookup_data = []

for v in velocities:
    x_hit = simulate_projectile(v, theta, target_height)
    if x_hit is not None:
        lookup_data.append((x_hit, v))

lookup_data.sort(key=lambda row: row[0])

with open("ballistic_lookup.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["distance_m", "velocity_m_per_s"])
    writer.writerows(lookup_data)