from collections import Counter

def minWindow(s: str, t: str)-> str:

    if not t:
        return ""

    countT = Counter(t)
    window = {}

    have, need = 0, len(countT)

    res, res_len = [-1, -1], float('inf')

    l = 0

    for r in range(len(s)):
        c = s[r]

        window[c] = window.get(c,0) + 1

        if c in countT and window[c]== countT[c]:
            have += 1

        while have == need:
            # update result

            if (r-l+1)< res_len:
                res = [l,r]
                res_len = r - l + 1

            # shrink window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1

            l += 1

    l, r = res
    return s[l:r+1] if resLen != float("inf") else ""
