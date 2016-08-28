# Equations Developed by Edward Lorenz and Published in his 1963 Paper "Deterministic Nonperiodic Flow"
# Inspired by: http://matplotlib.org/examples/mplot3d/lorenz_attractor.html
#
# This program was made in order to help me learn more about the Lorenz Equations, Python, and matplotlib
# Go read "Chaos: Making a New Science" if you want to read about Chaos Theory (including Lorenz)
#
# Note: Some variable are intentionally long/overly descriptive (e.g. "x" vs "x_point") for readability 
# and explainability to those who are not programmers (as well as for myself so that each variable or 
# parameter is easy to keep track of)

__author__ = "github.com/liamnickell"

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

num_of_points = 9250

def get_points(x, y, z, sigma=10.0, rho=28.0, beta=8.0/3.0, time=0.01):
	x_point = time * (sigma * (y - x))
	y_point = time * (x * (rho - z) - y)
	z_point = time * ((x * y) - (beta * z))

	return x_point, y_point, z_point


def main():
	x_points, y_points, z_points = [0.0], [1.0], [1.05]

	for i in range(num_of_points):
		new_x, new_y, new_z = get_points(x_points[i], y_points[i], z_points[i])
		x_points.append(x_points[i] + new_x)
		y_points.append(y_points[i] + new_y)
		z_points.append(z_points[i] + new_z)

	fig = plt.figure()
	ax = fig.gca(projection='3d')

	ax.plot(x_points, y_points, z_points)
	ax.set_xlabel("X Axis")
	ax.set_ylabel("Y Axis")
	ax.set_zlabel("Z Axis")
	ax.set_title("Lorenz Attractor")

	plt.show()


if __name__ == "__main__":
	main()