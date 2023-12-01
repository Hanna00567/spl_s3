import math
import random
import numpy as np

a = 1.21
b = 0.371


def form(x):
    y = (np.tan(a + b) ** 2 - (a + 1.5) ** (1 / 3) + a * b ** 5 - b / np.log(a ** 2))
    return y


print(form(9601.743376458367))

X = np.array([[1, random.randint(18, 30), random.randint(60, 82)] for i in range(12)])
print(X)
Y = np.array([[random.uniform(13.5, 18.6)] for i in range(12)])
print(Y)
A = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))
print(A)
Y2 = A[0] + A[1] * X[:, 1] + A[2] * X[:, 2]
print(Y2)
