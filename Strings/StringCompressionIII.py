
def string_compressionIII(s: str)->str:

    res = []
    pos = 0

    while pos < len(s):
        curr_count = 0
        curr_char = s[pos]
        while (pos < len(s) and curr_count < 9 and s[pos] == curr_char):
            curr_count += 1
            pos += 1

        res.append(str(curr_count))
        res.append(curr_char)

    return "".join(res)




if __name__ == '__main__':

    a = "aaaaaaaaaaaaaabb"

    print(string_compressionIII(a))
