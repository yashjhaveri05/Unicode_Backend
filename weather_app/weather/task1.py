def Task1(x,y):
    dictionary = {}
    for i in range(x, y):
        dictionary[i] = "11" in bin(i)[2:]
    return dictionary