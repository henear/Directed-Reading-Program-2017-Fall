from __future__ import division
import numpy as np
import matplotlib.pyplot as plt 
import numpy.linalg as la
import random as r


# monte carlo method solve pde

global dimension
dimension = 200

def uxxuyy(x, y):
	return 12 * (x ** 2 + y ** 2)
	# return -8 * np.pi * np.pi * np.cos(2*np.pi*y)*np.sin(2 * np.pi * x)

def main():
	# Initialize Variables:
	
	initVal = np.zeros((dimension+1, dimension+1))
	for i in range(1, dimension):
		# initVal[i, 0] =  ((dimension - i) * 1.0 / dimension ) ** 4
		x = 0
		y = 1 - dimension * i
		initVal[i, 0] = np.sin(2*np.pi*x)*np.cos(2*np.pi*y)
	print(initVal)
	for i in range(0, dimension):
		initVal[i, -1] = initVal[i, 0] + 1
	for i in range(1, dimension):
		initVal[-1, i] = (i* 1.0 / dimension) ** 4
	for i in range(0, dimension):
		initVal[0, i] = 1 + initVal[-1, i]
	initVal[-1, -1] = 1
	# print(initVal)
	#mySol = monteCarlo(initVal)
	actualSol = answer(initVal)
	#print("~~~My Sol~~~")
	# print(mySol)
	# print("~~~Actual Sol~~~")
	# print(actualSol)
	# print("~~~Diff of Sols~~")
	# print(la.norm(mySol - actualSol))
	xaxis = np.linspace(0, 1, dimension+1)
	yaxis = np.linspace(0, 1, dimension+1)
	plt.figure(1)
	plt.legend(loc = 'best')
	plt.clabel(plt.contour(xaxis, yaxis, actualSol), inline=1, fontsize=10)
	#plt.figure(2)
	#plt.clabel(plt.contour(xaxis, yaxis, mySol), inline=1, fontsize=10)
	plt.show()

def answer(initVal):
	ans = initVal
	for i in range(1, dimension):
		for j in range(1, dimension):
			x = i * 1.0 / dimension
			y = 1 - j * 1.0 / dimension
			ans[i, j] = x ** 4 + y ** 4
	return ans

def findExits(initVal, curri, currj):
	while 0 < curri < dimension and 0 < currj < dimension:
		temp = r.randint(0, 3)
		if temp == 0:
			curri -= 1
		elif temp == 1:
			curri += 1
		elif temp == 2:
			currj -= 1
		else:
			currj += 1
	# break Here
	# print("curri is " + str(curri))
	# print("currj is " + str(currj))
	x = curri * 1.0 / dimension
	y = 1 - (currj * 1.0 / dimension)
	return uxxuyy(x, y)

def findExpectation(curri, currj, initVal):
	numIter = 10
	Expects = 0
	for i in range(numIter):
		Expects += 1.0 * findExits(initVal, curri, currj) / numIter
	return Expects


def monteCarlo(initVal):
	result = initVal
	for i in range(1, dimension):
		for j in range(1, dimension):
			# Consider the point at dimension[i, j]
			curri = i
			currj = j
			result[i, j] = findExpectation(curri, currj, initVal)
	return result
			

main()