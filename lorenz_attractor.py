# Program Name: Lorenz Attractor
# Program Purpose: Graph the Lorenz Attractor using numpy and matplotlib modules
# Program Creation Date: 8/26/16
# Last Updated: 8/27/16
# Inspired by: http://matplotlib.org/examples/mplot3d/lorenz_attractor.html
# Equations Developed by Edward Lorenz and Published in his 1963 Paper "Deterministic Nonperiodic Flow"


__author__ = "github.com/liamnickell"

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

num_of_points = 8000

def get_points(x, y, z, sigma=10.0, rho=28.000001, beta=8.0/3.0, time=0.01):
	x_point = time * (sigma * (y - x))
	y_point = time * (x * (rho - z) - y)
	z_point = time * ((x * y) - (beta * z))

	return x_point, y_point, z_point


def main():
	xs, ys, zs = [0.0], [1.0], [1.05]

	for i in range(num_of_points):
		new_x, new_y, new_z = get_points(xs[i], ys[i], zs[i])
		xs.append(xs[i] + new_x)
		ys.append(ys[i] + new_y)
		zs.append(zs[i] + new_z)

	fig = plt.figure()
	ax = fig.gca(projection='3d')

	ax.plot(xs, ys, zs)
	ax.set_xlabel("X Axis")
	ax.set_ylabel("Y Axis")
	ax.set_zlabel("Z Axis")
	ax.set_title("Lorenz Attractor")

	plt.show()


if __name__ == "__main__":
	main()