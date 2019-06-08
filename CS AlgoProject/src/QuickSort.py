# uses python list manipulation:
def quickSort(L):
    # if there's less than two items it's already sorted
    if len(L) <= 1:
        return L
    #two pointer approach to find actual pivot location
    i, j = 0, len(L)-1
    while i != j:
        if i < j:
            if L[i] > L[j]: # swap:
                L[i], L[j] = L[j], L[i]
                i, j = j, i
            else:
                i += 1
        else:
            if L[i] < L[j]: # swap:
                L[i], L[j] = L[j], L[i]
                i, j = j, i
            else:
                i -= 1
    return quickSort(L[:i])+[L[i]]+quickSort(L[i+1:]) # divide and conquer
