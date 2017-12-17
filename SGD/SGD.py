import numpy as np
import numpy.random as npr
import math
import random
import matplotlib.pyplot as plt
# Solve for dxt = b(xt)dt + sigma(xt)d(Bt)
# Solve for black schole


def actualSol(x0, numPts, intervalLength,r, sigma):
	print(x0)
	ans = list()
	brownianlist = list()
	for i in range(numPts):
		if i == 0:
			brownianlist.append(npr.normal(0, intervalLength))
		else:
			brownianlist.append(brownianlist[-1] + npr.normal(0, intervalLength))
	x = list()
	for i in range(numPts):
		x.append(i)

	print(brownianlist)
	for i in range(numPts):
		tVal = i * intervalLength
		ans.append(x0*math.exp((r - 0.5 * sigma ** 2)*tVal + sigma*brownianlist[i]))
	print(ans)
	return ans

def	stochasticSol(x0, numPts, intervalLength, r, sigma):
	result = [0.0] * numPts
	result[0] = x0

	for i in range(1,numPts):
		result[i] = result[i-1] + r * intervalLength + sigma * npr.normal(0, math.sqrt(intervalLength))
	print(result)
	return result

def param():
	x0 = 0.1
	numPts = 1000
	intervalLength = 1.0/ numPts
	r = 1
	sigma = 1
	a = actualSol(x0, numPts, intervalLength, r, sigma)
	b = stochasticSol(x0, numPts, intervalLength, r, sigma)

	diff = 0
	for i in range(numPts):
		diff += (a[i] - b[i]) ** 2
	print(diff)
	c = list()
	for i in range(numPts):
		c.append(i*1.0/numPts)
	plt.plot(c, b)
	plt.show()





param()
