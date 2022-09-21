def multiply(n, a):
    if n == 1:
        return a
    return multiply(n-1, a) + a


print(multiply(5, 4))
