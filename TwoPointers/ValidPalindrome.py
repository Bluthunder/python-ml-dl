def isPalindrome(s: str)-> bool:
    new_s = ""

    for c in s:
        if c.isalnum():
            new_s += c.lower()

    return new_s == new_s[::-1]


def isPalindrome_2(s: str)-> bool:
    l , r = 0, len(s) -1

    while l < r :
        while l < r and not s[l].isalnum():
            l += 1

        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l , r = l + 1 , r - 1

    return True



if __name__ == '__main__':
    print(isPalindrome_2("A man, a plan, a canal: Panama"))
