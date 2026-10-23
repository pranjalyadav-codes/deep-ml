import numpy as np

def lu_decomposition(A: list) -> tuple:
    """
    Perform LU decomposition on a square matrix using Doolittle's method.
    """
    A = np.array(A, dtype=float)
    n = A.shape[0]

    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        # Calculate the ith row of U
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])

        # Calculate the ith column of L
        for j in range(i + 1, n):
            L[j, i] = (
                A[j, i] - np.dot(L[j, :i], U[:i, i])
            ) / U[i, i]

    return L, U