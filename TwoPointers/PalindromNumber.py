
def isPalindrome(num: int)->bool:

    if num < 0 :
        return False

    reverse = 0
    temp = num

    while temp != 0:
        digit = temp % 10
        reverse = (reverse * 10) + digit
        temp = temp // 10

    return reverse == num



if __name__ == '__main__':
    num = 123321

    print(isPalindrome(num))
