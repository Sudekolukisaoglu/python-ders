# bir dizinin tersi
import numpy as np

arr1 = np.arange(1,11)
print(arr1)
arr1 = arr1.reshape(5,2)
print(arr1)

tersi = arr1[::-1]
# print("Dizi :\n",arr1)
print("Tersi:\n",tersi)
