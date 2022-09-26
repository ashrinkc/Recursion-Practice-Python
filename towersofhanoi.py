def tower(n, source, destination, helper):
    if n == 1:
        print("move  disk 1 from  source", source,
              "to destination", destination)
        return
    tower(n-1, source, helper, destination)
    print("move disk", n, "from ", source, "to", destination)
    tower(n-1, helper, destination, source)


n = 3

tower(n, 'A', 'C', 'B')
