
def LCS(X:str, Y:str) -> int:

    dp = [[0 for j in range(len(Y) + 1)] for i in range(len(X) + 1)]

    for i in range(len(X) - 1, -1, -1):
        for j in range(len(Y)-1, -1, -1):
            if X[i] == Y[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])

    # print(dp)
    return dp[0][0]


"""
To get the string as well we can use backtracking. This is memory efficient for large strings
"""

def LCSString(X, Y):

    dp = [[0 for j in range(len(Y) + 1)] for i in range(len(X) + 1)]

    for i in range(len(X) - 1, -1, -1):
        for j in range(len(Y)-1, -1, -1):
            if X[i] == Y[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])

    results = []
    i, j  = 0, 0
    while i < len(X) and j < len(Y):
        if X[i] == Y[j]:
            results.append(X[i])
            i += 1
            j += 1
        elif dp[i+1][j] > dp[i][j+1]:
            i += 1
        else:
            j += 1

    return dp[0][0], ''.join(results)

def LCSString2(X,Y):

    dp = [['' for j in range(len(Y)+1)] for i in range(len(X) + 1)]

    for i in range(len(X)-1, -1, -1):
        for j in range(len(Y)-1, -1, -1):
            if X[i] == Y[j]:
                dp[i][j] = X[i] + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j],key=len)

    return len(dp[0][0]), dp[0][0]


if __name__ == '__main__':
    X = 'thisislatest'
    Y = 'testingLCS123testing'
    print(LCSString2(X,Y))
