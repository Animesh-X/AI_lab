import numpy as np
import time

m = int(input(f"Enter no of row of 1st matrix: "))
n = int(input(f"Enter no of col of 1st matrix: "))

p = int(input(f"Enter no of row of 2nd matrix: "))
q = int(input(f"Enter no of col of 2nd matrix: "))

start = time.process_time()
matrixA = np.random.normal(loc = 0, scale = 1, size = (m,n))
matrixB = np.random.uniform(low=0, high=1, size=(p, q))
end = time.process_time()



print("\nMatrix A:\n",matrixA,"\n")
print("Matrix B:\n",matrixB,"\n")
print("Time taken to create Matrices", (end - start) * 10**3, "ms.")

start = time.process_time()
try:
    inverse_matrixA = np.linalg.inv(matrixA)
    inverse_matrixB = np.linalg.inv(matrixB)
except:
    raise Exception("Cannot Inverse non-square Matrix")
else:
    print("\nInverse of  Matrix A is:\n",inverse_matrixA,"\n")
    print("Inverse of Matrix B is:\n",inverse_matrixB,"\n")
end = time.process_time()
print("Time taken to Inverse Matrices", (end - start) * 10**3, "ms.")

start = time.process_time()
try:
    product_inverse = np.dot(inverse_matrixA, inverse_matrixB)
except:
    raise Exception("Error Multiplying the Matrices")
else:
    print("\nProduct of Inverses:\n",product_inverse)
end = time.process_time()
print("\nTime taken to Multiply Matrices", (end - start) * 10**3, "ms.")


start = time.process_time()
try:
    transpose_matrixA = np.transpose(matrixA)
    transpose_matrixB = np.transpose(matrixB)
except:
    raise Exception("Cannot Transpose Matrix")
else:
    print("\nTranspose of  Matrix A is:\n",transpose_matrixA,"\n")
    print("Transpose of Matrix B is:\n",transpose_matrixB,"\n")
end = time.process_time()
print("Time taken to tanspose Matrices", (end - start) * 10**3, "ms.")

start = time.process_time()
try:
    product_transpose = np.dot(transpose_matrixA, transpose_matrixB)
except:
    raise Exception("Error Multiplying the Matrices")
else:
    print("\nProduct of Transpose:\n",product_transpose)
end = time.process_time()
print("\nTime taken to Multiply Matrices", (end - start) * 10**3, "ms.")




