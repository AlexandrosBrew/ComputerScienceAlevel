import numpy as np
matrix1 = np.array([])
matrix2 = np.array([])
h1 = int(input("Enter height of matrix1: "))
w1 = int(input("Enter width of matrix1: "))
h2 = int(input("Enter height of matrix2: "))
w2 = int(input("Enter width of matrix2: "))
matrix1.reshape(w1, h1)
matrix2.reshape(w2, h2)


print(len(matrix1))