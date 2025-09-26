
def  is_subsequence(s: str, t: str)->bool:

    ptr1 = 0

    ptr2 = 0

    while ptr1 < len(s) and ptr2 < len(t):
        if s[ptr1] == t[ptr2]:
            ptr1 += 1
        ptr2 += 1

    return ptr1 == len(s)



if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"


    print(is_subsequence(s, t))
