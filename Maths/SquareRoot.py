"""
    Newton Raphson Rule
    Rn+1 = (Rn + x/Rn) / 2

    This function uses Newton Raphson to find square root and if not a perfect square should return nearest integer. No in built method is used.

"""
def square_root(x: int) -> int:

    if x < 0 :
        raise ValueError ("Non negative Number")


    if x == 0 or x == 1:
        return 1

    guess = x / 2.0
    epsilon = 1e-6

    while abs(guess*guess - x) > epsilon:
        guess = (guess + x/guess) / 2.0

    return int(guess)


if __name__ == "__main__":

    print(f'Square Root of Number is ---> {square_root(190)}')

    # checking with using in built exponentiation
    print(f'Square Root of Number is ---> {int(190**0.5)}')
