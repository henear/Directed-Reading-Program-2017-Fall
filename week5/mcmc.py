from __future__ import division
import numpy as np
import matplotlib.pyplot as plt 
import numpy.linalg as la
import random as r
import math


	# monte carlo method solve pde

global dimension
dimension = 10
def getVal(x, y):
	return 1.0/(x*y + 0.0001)

def uxxuyy(x, y):
	# return 12 * (x ** 2 + y ** 2)
	return 0

def main():
	# Initialize Variables:
	xaxis = np.linspace(0, 1, dimension+1)
	yaxis = np.linspace(0, 1, dimension+1)

	initVal = np.zeros((dimension+1, dimension+1))
	for i in range(dimension+1):
		
		x = 0
		y = 1 -  i*1.0/dimension
		initVal[i, 0] =  getVal(x, y)
	print("1")
	print(initVal)
	for i in range(dimension+1):
		x = 1
		y = 1 - i * 1.0 / dimension
		initVal[i, -1] = getVal(x, y)
	print("2")
	print(initVal)
	for i in range(1, dimension):
		x = i * 1.0 / dimension
		y = 1
		initVal[0, i] = getVal(x, y)
	print("3")
	print(initVal)
	for i in range(0, dimension):
		# x = i / (1.0 * dimension)
		# y = 0
		# initVal[0, i] = np.sin(2*np.pi*x)*np.cos(2*np.pi*y)
		x = i * 1.0 / dimension
		y = 0
		initVal[-1, i] = getVal(x, y)
	print("4")
	print(initVal)
	print(initVal)
	mySol = monteCarlo(initVal)
	actualSol = np.copy(answer(initVal))
	print("~~~My Sol~~~")
	print(mySol)
	print("~~~Actual Sol~~~")
	print(actualSol)
	print("~~~Diff of Sols~~")
	print("error term:")
	print(la.norm(mySol - actualSol))
	
	plt.figure(1)
	plt.legend(loc = 'best')
	plt.clabel(plt.contour(xaxis, yaxis, actualSol), inline=1, fontsize=10)
	plt.figure(2)
	plt.legend(loc = 'best')
	plt.clabel(plt.contour(xaxis, yaxis, mySol), inline=1, fontsize=10)
	plt.show()

def answer(initVal):
	ans = initVal
	yaxis = 1. - np.linspace(0, 1, dimension+1)
	# for i in range(1, dimension):
	# 	# for j in range(1, dimension):
	# 		x = i * 1.0 / dimension
	# 		# y = 1 - j * 1.0 / dimension
	# 		ans[i, :] = math.sin(2*math.pi*x) *np.cos(2*math.pi*yaxis[:])
	# return ans
	for i in range(1, dimension):
		for j in range(1, dimension):
			x = i * 1.0 / dimension
			y = 1 - j * 1.0 / dimension
			ans[i, j] = getVal(x, y)
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
	currVal = getVal(x, y)
	return currVal

def findExpectation(curri, currj, initVal):
	numIter = 1000
	Expects = 0
	for i in range(numIter):
		Expects += 1.0 * findExits(initVal, curri, currj) / numIter
	return Expects


def monteCarlo(initVal):
	result = np.copy(initVal)
	xaxis = np.arange(0, dimension+1)
	yaxis = np.arange(0, dimension+1)

	for i in range(1, dimension):
		for j in range(1, dimension):
			# Consider the point at dimension[i, j]
			curri = i
			currj = j
			result[i, j] = findExpectation(curri, currj, initVal)
	return result
			
main()
