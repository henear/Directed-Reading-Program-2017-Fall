import numpy as np
import math
import random


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
	for i in range(100):
		# result += estimatepi(num*100)
		currPi = estimatepi(size*100)
		currError = abs(currPi - math.pi)
		totalError += currError

	totalError = totalError *0.01
	return totalError

def hh():
	cand = [1,2,4,8,16,32,64,128,256,512,1024]
	errorlist = list()
	for i in cand:
		currError = allfindPi(i)
		errorlist.append(currError)
		print(currError)

	for i in range(len(cand)-1):
		ratio = errorlist[i+1]*1.0 / errorlist[i]
		print(math.log(ratio, 2)


hh()
