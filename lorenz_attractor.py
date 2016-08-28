# Equations Developed by Edward Lorenz and Published in his 1963 Paper "Deterministic Nonperiodic Flow"
# Inspired by: http://matplotlib.org/examples/mplot3d/lorenz_attractor.html
#
# This program was made in order to help me learn more about the Lorenz Equations, Python, and matplotlib
# Go read "Chaos: Making a New Science" if you want to read about Chaos Theory (including Lorenz)

__author__ = "github.com/liamnickell"

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def get_values(x, y, z, sigma=10.0, rho=28.0, beta=8.0/3.0, time=0.01):
	x_point = time * (sigma * (y - x))
	y_point = time * (x * (rho - z) - y)
	z_point = time * ((x * y) - (beta * z))

	return x_point, y_point, z_point


def generate_points(points=9000):
	xs, ys, zs = [0.0], [1.0], [1.05]

	for i in range(points):
		new_x, new_y, new_z = get_values(xs[i], ys[i], zs[i])
		xs.append(xs[i] + new_x)
		ys.append(ys[i] + new_y)
		zs.append(zs[i] + new_z)

	return xs, ys, zs


def main():
	xs, ys, zs = generate_points()

	fig = plt.figure()
	ax = fig.gca(projection='3d')

	ax.plot(xs, ys, zs)
	ax.set_title("Lorenz Attractor")
	ax.set_xlabel("X Axis")
	ax.set_ylabel("Y Axis")
	ax.set_zlabel("Z Axis")

	plt.show()


if __name__ == "__main__":
	main()