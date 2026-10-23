import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    A = np.array(matrix)

    if A.shape[1] != A.shape[0]:
        return None

    det_A = round(np.linalg.det(A), 1)
    if det_A == 0:
        return None

    inv_A = np.linalg.inv(A)
    return inv_A
    