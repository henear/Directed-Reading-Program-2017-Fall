import numpy as np
import scipy
import numpy.linalg as la
import matplotlib.pyplot as plt

dimension = 100

# x = [0] * dimension
# x[0] = 1
# x[-1] = 2
x = np.zeros((dimension, 1))
x[0, 0] = 1
x[dimension-1, 0] = 2
Diagonal = np.zeros((dimension, dimension))
Lower = np.zeros((dimension, dimension))
Upper = np.zeros((dimension, dimension))
InverseD = np.zeros((dimension, dimension))
Diagonal[0, 0] = 1
Diagonal[dimension-1, dimension-1] = 1
IterNums = 200000000

for i in range(dimension):
	Diagonal[i, i] = 2
for i in range(1, dimension):
	Lower[i, i-1] = 1
for i in range(0, dimension-1):
	Upper[i, i+1] = 1
# print(Diagonal)
for i in range(dimension):
	InverseD[i, i] = 1.0 / Diagonal[i, i]

b = x
#
y = np.linspace(0,1,dimension)
for i in range(IterNums):
	
	xnew = np.dot(np.dot(InverseD, np.add(Lower, Upper)), x) + np.dot(InverseD, b)
	if la.norm(np.subtract(x, xnew)) < 10 ** -3:
		print("num Of Iter: " + str(i))
		break
	
	x = xnew

plt.plot(y, x)
plt.show()
print(x)
