def merge(left, right):
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
