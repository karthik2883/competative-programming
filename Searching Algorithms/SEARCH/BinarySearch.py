def BinarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = int((left + right // 2))
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


a = [10, 20, 30, 45, 55, 60]
print(BinarySearch(a, 99))
