import numpy as np
import matplotlib.pyplot as plt

# Define flow conditions
M_inf = 2.0  # Freestream Mach number
gamma = 1.4  # Specific heat ratio (for air)

# Define the number of points in both the x and y directions for the 2D grid
num_x_points = 100
num_y_points = 100

# Create a 2D grid of points on the airfoil's surface (x, y)
x_airfoil = np.linspace(0, 1, num_x_points)
y_airfoil = np.linspace(0, 1, num_y_points)

#x_airfoil = np.linspace(-1, 1, num_x_points)  # Varying from -1 to 1
#y_airfoil = np.sqrt(1 - x_airfoil**2)  # Half-circle equation y = sqrt(1 - x^2)

# Initialize arrays to store Mach numbers and shock wave positions (2D arrays)
Mach_numbers = np.zeros((num_x_points, num_y_points))
shock_wave_positions_x = np.zeros((num_x_points, num_y_points))
shock_wave_positions_y = np.zeros((num_x_points, num_y_points))

# Geometry-dependent function for shock wave position calculation
def calculate_shock_wave_position(x, y):
    # Example: Simple wedge-shaped airfoil with a 30-degree half-angle
    theta_half = np.radians(30)
    shock_position_x = x - y * np.tan(theta_half)
    shock_position_y = y
    return shock_position_x, shock_position_y

# Calculate Mach numbers and shock wave positions
for i in range(num_x_points):
    for j in range(num_y_points):
        # Calculate Mach number at each point
        x_position = x_airfoil[i]
        y_position = y_airfoil[j]

        Mach_numbers[i, j] = M_inf / np.sqrt(1 + ((2 * gamma) / (gamma - 1)) * (M_inf**2 - 1) * x_position)
        
        # Calculate shock wave positions based on the geometry-dependent function
        shock_wave_positions_x[i, j], shock_wave_positions_y[i, j] = calculate_shock_wave_position(x_position, y_position)

# Create a 2D visualization of the Mach number distribution (e.g., contour plot)
plt.figure(figsize=(10, 6))
plt.contourf(x_airfoil, y_airfoil, Mach_numbers, levels=50, cmap='viridis')
plt.colorbar(label='Mach Number')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('2D Mach Number Distribution around Airfoil')

# Plot shock wave positions on the visualization
plt.scatter(shock_wave_positions_x, shock_wave_positions_y, c='red', marker='o', label='Shock Wave Positions')

# Add labels, legend, and display the plot
plt.legend()
plt.show()