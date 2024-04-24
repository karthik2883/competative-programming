def QuickSort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a.pop()

    greater = []
    lower = []
    for i in a:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)

    return QuickSort(lower) +[pivot]+ QuickSort(greater)

l = [1,2,0]
print(QuickSort(l))
#nlog(n)_
