#



def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibM(n, memo):
    if n==1:
        return 0
    if n == 2:
        return 1

    if not n in memo:
        memo[n] = fibM(n-1, memo)  + fibM(n-2, memo)

    return memo[n]



def fibT(n):
    tb = [0,1]
    for i in range(2, n+1):
        tb.append(tb[i-1] + tb[i-2])

    return tb[n-1]



    
