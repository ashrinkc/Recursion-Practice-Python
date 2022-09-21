def list_sum(alis):
    if len(alis) == 0:
        return 0
    return alis[0] + list_sum(alis[1:])


print(list_sum([2, 10, 5]))
