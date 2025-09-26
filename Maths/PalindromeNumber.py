def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10

    # For odd number of digits, drop the middle digit in rev
    return x == rev or x == rev // 10
