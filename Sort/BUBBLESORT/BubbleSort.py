def BubbleSort(a):
    s = len(a)
    for i in range(s):
        swapped = False
        for j in range(0, s - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
            if not swapped:
                break

arr = [32,34,3,23,4,5,5,7,55,3]
BubbleSort(arr)
print(arr)


