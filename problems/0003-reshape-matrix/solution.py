import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    matrix = np.array(a)
    if matrix.size != new_shape[0] * new_shape[1]:
        return []
    # Reshape the matrix
    reshaped_matrix = matrix.reshape(new_shape)

    # Convert back to a Python list
    return reshaped_matrix.tolist()