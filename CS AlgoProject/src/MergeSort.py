def mergeSort(L):
    if len(L) > 1:
        mid = len(L)//2 # gets middle index
        # recursively sorts and returns the left and right halves
        left = mergeSort(L[:mid])
        right = mergeSort(L[mid:])
        # uses a two pointer approach to sort the remaining two lists
        out, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
        if i < len(left):
            out += left[i:]
        if j < len(right):
            out += right[j:]
        return out
    return L # returns original string if length less than or equal to one
