import numpy as np
import math
import random
import matplotlib.pyplot as plt


# Estimating PI

def estimatepi(size):
	count = 0
	for i in range(size):
		a = random.uniform(0,1)
		b = random.uniform(0,1)
		if a**2 + b**2 <=1:
			count+=1
	return count*4/size

def allfindPi(size):
	totalError = 0
	for i in range(1000):
		# result += estimatepi(num*100)
		currPi = estimatepi(size*100)
		currError = abs(currPi - math.pi)
		totalError += currError

	totalError = totalError *0.001
	return totalError


cand = [1,2,4,8,16,32,64,128,256,512,1024]
ratiolist = list()
errorlist = list()
for i in cand:
	currError = allfindPi(i)
	errorlist.append(currError)
	print(currError)

for i in range(len(cand)-1):
	ratio = errorlist[i+1]*1.0 / errorlist[i]
	ratiolist.append(math.log(ratio, 2))
	print(math.log(ratio, 2))
cand = [1,2,3,4,5,6,7,8,9,10]
plt.plot(cand, ratiolist)
plt.show()




