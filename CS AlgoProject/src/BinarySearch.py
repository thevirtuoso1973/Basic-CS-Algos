# uses pointers:
def binarySearch(L, target, start, end):
    if start == end and L[start] != target:
        return -1
    mid = (end-start)//2 + start
    if L[mid] == target:
        return mid
    elif L[mid] > target:
        return binarySearch(L, target, start, mid - 1)
    else:
        return binarySearch(L, target, mid + 1, end)
