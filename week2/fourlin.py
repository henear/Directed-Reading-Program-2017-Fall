import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la


def fourlin():
	numOfIter = 10000
	dimension = 25
	result = np.zeros((dimension+1, dimension+1))
	for i in range(dimension+1):
		result[i, 0] = - 4.0 * i / dimension + 8
		result[i, -1] = - 4.0 * i / dimension + 11
		result[0, i] = 3.0 * i/ dimension + 8
		result[-1, i] = 3.0 * i / dimension + 4
	print(result)
	
	result2 = np.copy(result)
	for myIter in range(numOfIter):
		for i in range(1, dimension):
			for j in range(1, dimension):
				result2[i, j] = 0.25 * (result[i, j + 1] + result[i, j-1] + result[i-1, j] + result[i+1, j])

		if la.norm(result - result2) < 10 ** -15:
			print("num of iter: " + str(myIter))
			break
		result = np.copy(result2)
	x = np.linspace(0, 1, dimension+1)
	y = np.linspace(0, 1, dimension+1)
	
	plt.clabel(plt.contour(x,y,result), inline=1, fontsize=10)
	plt.show()

fourlin()