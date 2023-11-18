import numpy as np

delta_vertical_positions = np.diff(vertical_positions)
delta_time_intervals = np.diff(time_intervals)

average_velocity = delta_vertical_positions / delta_time_intervals

print("Change in Vertical Position:", delta_vertical_positions)
print("Change in Time Intervals:", delta_time_intervals)
print("Average Velocity:", average_velocity)
