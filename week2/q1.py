import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la

def main():
	numOfIter = 10000
	dimension = 100
	result = np.zeros((dimension+1, dimension+1))
	for i in range(dimension+1):
		result[i, 0] = 3 - (3.0 / (dimension)) * i

	for i in range(dimension+1):
		result[-1, i] = 2.0 * i / dimension
	for i in range(dimension+1):
		result[i, -1] = 4 - 2.0 * i / dimension
	for i in range(dimension+1):
		result[0, i] = 3 + 1.0 * i / dimension
	print(result)
	result2 = np.copy(result)
	for myIter in range(numOfIter):
		for i in range(1, dimension):
			for j in range(1, dimension):
				result2[i, j] = 0.25 * (result[i, j + 1] + result[i, j-1] + result[i-1, j] + result[i+1, j])
		if myIter % 100 == 0:
			print(la.norm(result - result2))
		if la.norm(result - result2) < 10 ** -10:
			print("num of iter: " + str(myIter))
			break
		result = np.copy(result2)
	x = np.linspace(0, 1, dimension+1)
	y = np.linspace(0, 1, dimension+1)
	
	plt.clabel(plt.contour(x,y,result), inline=1, fontsize=10)
	plt.show()
	
main()