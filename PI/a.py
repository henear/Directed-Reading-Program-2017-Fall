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

def allfindPi(num):
	result = 0
	for i in range(100):
		result += estimatepi(num*100)
	result = result*0.01
	return result

cand = [1,2,4,8,16,32,64,128,256,512,1024]
errorlist = list()
for i in cand:
	error = abs(allfindPi(i) - math.pi)
	errorlist.append(error)
for i in range(len(errorlist)-1):
	print(errorlist[i+1]*1.0 / errorlist[i])
