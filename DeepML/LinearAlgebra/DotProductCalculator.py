import numpy as np

def calculate_dot_product(vec1, vec2)->float:
    """
    Calculates dot product of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing vector 1
        vec2 (numpy.ndarray): 1D array representing vector 2

    Returns:
        float: Dot product of vec1 and vec2
    """

    if vec1.shape != vec2.shape or vec1.ndim != 1 or vec2.ndim != 1:
        raise ValueError("Both inputs must be 1D Numpy Array of same length")

    return np.dot(vec1, vec2)



if __name__ == '__main__':
    vec1 = np.array([1, 2, 3])
    vec2 = np.array([4, 5, 6])
    result = calculate_dot_product(vec1, vec2)
    print(result)
