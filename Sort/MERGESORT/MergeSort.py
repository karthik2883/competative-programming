"""def merge(left, right):
    newArray = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            newArray.append(left[i])
            i +=1
        else:
            newArray.append(right[j])
            j +=1

    newArray.extend(left[i:])
    newArray.extend(right[j:])
    return newArray



def MergeSort(arr):
    if len(arr) <=1:
        return arr
    mid = int(len(arr)//2)
    l_half = MergeSort(arr[:mid])
    r_half = MergeSort(arr[mid:])
    return merge(l_half,r_half)


a =[45,3,34,3,33,22,24,3,557,754,4]
print(MergeSort(a))
"""


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < left and j < right:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend((left[i:])
    result.extend(right[j:])
    return result
