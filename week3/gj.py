import numpy as np
import matplotlib.pyplot as plt 
import numpy.linalg as la

# discruntize the input
def main():
	dimension = 5
	result = np.zeros((dimension + 1, dimension + 1))
	print(result)
	result[0, 0] = 1
	for i in range(1, dimension):
		result[i, 0] =  ((dimension - i) * 1.0 / dimension ) ** 4
	print(result)
main()