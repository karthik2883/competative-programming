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

a = [45, 1, 12, 121]
BubbleSort(a)
print(a)
