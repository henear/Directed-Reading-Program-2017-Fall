import numpy as np
import scipy
import numpy.linalg as la
import matplotlib.pyplot as plt

m = n = 5
Result = np.zeros((m+1, n+1))
# print(Result)

# first case: take all boundary of same value
boundaryconstant = 2
step = 1.0 / m
Result[:,0] = boundaryconstant
Result[:,-1] = boundaryconstant
Result[0,:] = boundaryconstant
Result[-1,:] = boundaryconstant
# for i in range(m+1):
# 	Result[i, 0] = boundaryconstant
# for i in range(n+1):
# 	Result[-1, i] = boundaryconstant
# for i in range(m+1):
# 	Result[i, -1] = boundaryconstant
# for i in range(n+1):
# 	Result[0, i] = boundaryconstant
# print(Result)
Result2 = np.copy(Result)
for myIter in range(1000):
	# Result2 = np
	for i in range(1, m):
		for j in range(1, n):
			Result2[i, j] =  1.0 / 4 * (Result[i - 1, j] + Result[i + 1, j] + Result[i, j - 1] + Result[i, j+1]) 
	# print(Result)
	# print(Result2)
	# print( "norm of diff is: ", la.norm(Result-Result2, 2))
	# print("~~~~~~~diff matrices ~~~~~~~~")
	# print(Result - Result2)
	# if myIter % 20 == 0 :
	# 	print(str(la.norm(Result)) + " " + str(la.norm(Result2)))
	if la.norm(Result - Result2) < 10**-13:
		print("num of iter: " + str(myIter))
		break

	
	Result = np.copy(Result2)
print("after")
# print(Result)
x = np.linspace(0, 1, m+1)
y = np.linspace(0, 1, n+1)
# plt.colorbar(im, orientation='horizontal', shrink=0.8)
plt.clabel(plt.contour(x,y,Result), inline=1, fontsize=10)
# plt.show()
