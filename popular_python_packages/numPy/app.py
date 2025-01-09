import numpy as np

array = np.zeros((3,5), dtype=int)
array = np.ones((3,5), dtype=int)
array = np.full((4, 5), 2, dtype=int)
array = np.random.random((3, 5))

print(array)
print(array > 0.2)
print(np.sum(array))
print("=========================================")
dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 3.4
print(dimensions_cm)
