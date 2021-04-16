import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.zeros((a.shape[0], a.shape[1], 3), dtype=np.uint8)
b[a == 1,0] = 255
print(b)