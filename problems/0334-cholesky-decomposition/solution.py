import numpy as np

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric positive-definite matrix.
    
    Args:
        A: A symmetric positive-definite matrix (2D list or numpy array)
    
    Returns:
        L: Lower triangular matrix such that A = L @ L.T as a 2D list,
           or -1 if decomposition is not possible
    """
    # Your code here
    try:
        A = np.array(A, dtype=float)

        # Check for empty or invalid matrices
        if A.ndim != 2 or A.shape[0] == 0:
            return -1

        # Check if the matrix is square
        if A.shape[0] != A.shape[1]:
            return -1

        # Check if the matrix is symmetric
        if not np.allclose(A, A.T):
            return -1

        # Perform Cholesky decomposition
        L = np.linalg.cholesky(A)

        return L.tolist()

    except (ValueError, TypeError, np.linalg.LinAlgError):
        return -1