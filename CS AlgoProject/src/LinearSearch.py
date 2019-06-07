def linearSearch(L, val): # array/list, value to search for
    for i in range(len(L)):
        if L[i] == val:
            return i
    return -1
