import numpy as np

arr = np.array([[1, 2], [5, 6]])  #Se crea la matriz
inverse_array = np.linalg.inv(arr)  #Se crea la inversa de la matriz
print("Inverse array is ")
print(inverse_array[0])
print()