
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float])->list[int|float]:
    """
    Calculates Matrix Vector dot product

    Args:
        a: Matrix with int or float values
        b: Vector with int or float values

    Returs:
        Dot product of a and b

    """

    if not a or len(a[0]) != len(b):
        return -1

    return [sum(row[j] * b[j] for j in range(len(b))) for row in a]


if __name__ == '__main__':
    a = [[1, 2], [2, 4]]
    b = [1, 2]

    result = matrix_dot_vector(a, b)
    print(result)
