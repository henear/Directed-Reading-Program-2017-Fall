import numpy as np
import matplotlib.pyplot as plt 
import numpy.linalg as la

# discruntize the input
global dimension
dimension = 4

def uxxuyy(x, y):
	# print("x is " + str(x))
	# print("y is " + str(y))
	return 12 * (x ** 2 + y ** 2)

def main():
	# dimension = 6
	initVal = np.zeros((dimension + 1, dimension + 1))
	
	initVal[0, 0] = 1
	# discruntize the variables
	for i in range(1, dimension):
		initVal[i, 0] =  ((dimension - i) * 1.0 / dimension ) ** 4
	for i in range(0, dimension):
		initVal[i, -1] = initVal[i, 0] + 1
	for i in range(1, dimension):
		initVal[-1, i] = (i* 1.0 / dimension) ** 4
	for i in range(0, dimension):
		initVal[0, i] = 1 + initVal[-1, i]
	initVal[-1, -1] = 1
	print(initVal)
	xaxis = np.linspace(0, 1, dimension+1)
	yaxis = np.linspace(0, 1, dimension+1)
	# Solve by Gauss-Jacobian
	f = np.zeros((dimension + 1, dimension + 1))
	f[:,:] = uxxuyy(xaxis[:],yaxis[:])
	# print(f)
	# gjResult = gj(initVal)
	# # Solve by Gauss-Seidel
	# gsResult = gs(initVal)
	# print("Gauss-Jacobian")
	# print(gjResult)
	# print("Gauss-Seidel")
	# print(gsResult)
	# print("Standard Solution")

	solution = np.copy(initVal)
	for i in ragne(1, dimension):
		for j in dimension(1, dimension):
			x = 1.0* i / dimension
			y = 1 -  1.0 * j / dimension
			solution[i, j] = x ** 4 + y ** 4
	print(solution)


def gj(initVal):
	gaph = 1.0 / dimension
	result = np.copy(initVal)
	for iterNum in range(100):
		for i in range(1, dimension):
			for j in range(1, dimension):
				x = i * gaph
				y = 1 - j * gaph
			# if i == 1 and j == 1:
			# 	print(uxxuyy(x, y))
				result[i, j] = - gaph * gaph * uxxuyy(x, y) + 0.25 * (initVal[i+1, j] + initVal[i-1, j] + initVal[i, j+1] + initVal[i, j-1])
		initVal = np.copy(result)
	# xaxis = np.linspace(0, 1, dimension+1)
	# yaxis = np.linspace(0, 1, dimension+1)
	# plt.clabel(plt.contour(xaxis, yaxis, result), inline=1, fontsize=10)
	# plt.show()
	return initVal



def gs(initVal):
	gaph = 1.0 / dimension
	for iterNum in range(100):
		for i in range(1, dimension):
			for j in range(1, dimension):
				x = i * gaph
				y = 1 - j * gaph
				initVal[i, j] = -gaph * gaph * uxxuyy(x, y) + 0.25 * (initVal[i-1, j] + initVal[i+1, j] + initVal[i, j-1] + initVal[i, j+1])

	# xaxis = np.linspace(0, 1, dimension+1)
	# yaxis = np.linspace(0, 1, dimension+1)
	# plt.clabel(plt.contour(xaxis, yaxis, initVal), inline=1, fontsize=10)
	# plt.show()
	return initVal

main()