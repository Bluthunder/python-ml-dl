import numpy as np

def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    """
    Calculates Transpose of a Matrix

    Args:
        a: Matrix

    Return:
        Matrix
    """
    nd_array = np.array(a)
    b = nd_array.transpose()

    return b.tolist()  # convert back to list if you want list output


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6]]
    print(transpose_matrix(a))
