def exponential(a, n):
    if n == 0:
        return 1
    return exponential(a, n-1) * a


print(exponential(5, 3))
