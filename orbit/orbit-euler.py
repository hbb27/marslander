import numpy as np
import matplotlib.pyplot as plt

# position vector, velocity vector, gravitational field constant, and mass of planet
x = np.array([5*(10**6), 0, 0])
v = np.array([0, 0, 0])    # for scenario 1-4, adjust v_y to 0, ~2926, ~3500, ~4200, respectively
G = 6.67*(10**(-11))
M = 6.42*(10**23)
r = 3390000

# simulation time, timestep and time
t_max = 50000
dt = 1
t_array = np.arange(0, t_max, dt)
num = len(t_array)

# initialise empty lists to record trajectories
position = np.zeros((num, 3))
velocity = np.zeros((num, 3))
altitude = np.zeros(num)
speed = np.zeros(num)

# Euler integration
for i, t in enumerate(t_array):

    # log current state to trajectories
    position[i] = x
    velocity[i] = v
    altitude[i] = np.linalg.norm(x)
    speed[i] = np.linalg.norm(v)

    # calculate new position and velocity
    a = (-(G * M) / altitude[i] ** 3) * x
    x = x + dt * v
    v = v + dt * a


# plot the altitude-time and velocity-time graph
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(t_array, altitude)
ax1.set_ylabel('altitude (m)')
ax1.grid()

ax2.plot(t_array, speed, color='orange')
ax2.set_xlabel('time (s)')
ax2.set_ylabel('speed (m/s)')
ax2.grid()

plt.show()

# AI generated code for 2-D visualisation of the trajectory (scenarios 2-4)
plt.figure()
plt.plot(position[:, 0], position[:, 1])
plt.axis('equal')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()

# Showing Mars,
theta = np.linspace(0, 2*np.pi, 100)
mars_x = 3390000 * np.cos(theta)
mars_y = 3390000 * np.sin(theta)
plt.plot(mars_x, mars_y, 'r-')

plt.show()