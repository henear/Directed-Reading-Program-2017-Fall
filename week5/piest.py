import math
import numpy as np
import numpy.linalg as la
def oneIns(numOfIter):
	count = 0
	for i in range(numOfIter):
		
		a = np.random.rand(1, 2)
		if la.norm(a) <= 1:
			count+=4
	error = abs(count*1.0/numOfIter - math.pi)
	print("curr Estimated Pi Value: " + str(count*1.0/numOfIter ))
	return error
		
def main():
	for i in range(1,20):
		a = oneIns((int)(i*10000))
		b = oneIns((int)(i*10000 + 10000))
		ratio = a / b
		print(math.log(ratio, (i+1)/(1.0*i)))

main()
