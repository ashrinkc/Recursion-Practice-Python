def strlen(val):
    if val == "":
        return 0
    return strlen(val[1:]) + 1


print(strlen("I am boy"))
