
def lengthOfLastWord(s:str) -> int:
    words = s.strip().split(" ")
    print(words)
    last_words = words[-1]
    print(last_words)
    return len(last_words)




if __name__ == '__main__':
    s = "Hello World"
    print(lengthOfLastWord(s))
