def nuke(n):
    a = []
    for i in range(10):
        if n > 1:
            a.append(nuke(n-1))
        else:
            a.append(n)
    return a
    
print(nuke(7))