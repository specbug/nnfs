import numpy as np

l = np.array([1, 2, 3]) # 1D array (vector)

lol = np.array([[1, 2, 3],
				[4, 5, 6]]) # 2D array (matrix)

lol_2 = np.array([[1, 2, 3],
				  [4, 5, 6],
				  [7, 8, 9]]) # 2D array (matrix)

lolol = np.array([
				  [[1, 2, 3, 0],
				   [4, 5, 6, 0]],
				  [[7, 8, 9, 0],
				   [10, 11, 12, 0]],
				  [[13, 14, 15, 0],
				   [16, 17, 18, 0]]
			     ]) # 3D array (matrix)

print(f'1D array l: {l.shape}')
print(f'2D array lol: {lol.shape}')
print(f'2D array lol_2: {lol_2.shape}')
print(f'3D array lolol: {lolol.shape}')