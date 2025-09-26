import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    # λ² - (a + d)λ + (ad - bc) = 0

    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input must be a 2x2 matrix")


    a, b = matrix[0]
    c, d = matrix[1]

    trace = a + d

    det = a * d - b * c

    # Characteristic equation: λ² - trace*λ + det = 0
    discriminant = trace ** 2 - 4 * det

    if discriminant < 0:
        raise ValueError("Matrix has complex eigenvalues")

    sqrt_disc = math.sqrt(discriminant)
    lambda1 = (trace + sqrt_disc) / 2
    lambda2 = (trace - sqrt_disc) / 2

    eigenvalues = sorted([lambda1, lambda2], reverse=True)


	return eigenvalues
