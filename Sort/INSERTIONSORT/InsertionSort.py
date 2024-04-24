# def InsertionSort(a):
#     s = len(a)
#     for i in range(1, s):
#         key = a[i]
#         j = i - 1
#         while j >= 0 and key < a[j]:
#             a[j + 1] = a[j]
#             j -= 1
#
#         a[j + 1] = key
#
#
# a = [45, 45, 58, 44, 56, 5]
# InsertionSort(a)
# print(a)


def InsertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


a = [45, 3, 23, 44, 22, 3, 443, 2]
InsertionSort(a)
print(a)
