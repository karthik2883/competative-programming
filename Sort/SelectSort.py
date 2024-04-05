def SelectionSort(a):
    s = len(a)
    for i in range(s - 1):
        mini = i
        for j in range(i + 1, s):
            if a[j] < a[mini]:
                mini = j

        a[i], a[mini] = a[mini], a[i]

arr = [12, 33, 99, 92, 1, 2, 3, 9]
SelectionSort(arr)
print(arr)
