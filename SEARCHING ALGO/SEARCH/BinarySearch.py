# def BinarySearch(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = int((left + right // 2))
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1
#
#
# a = [10, 20, 30, 45, 55, 60]
# print(BinarySearch(a, 55))

def BinarySearch(arr, target):
    arr.sort()
    l = []
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(mid)
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


a = [10, 20, 30, 45, 55, 60]
target = 30
print(BinarySearch(a, target))

# def binary_search(arr, target):
#     # Initialize pointers for the start and end of the array
#     left, right = 0, len(arr) - 1
#
#     # Iterate until the left pointer is less than or equal to the right pointer
#     while left <= right:
#         # Calculate the middle index
#         mid = (left + right) // 2
#
#         # Check if the target is found at the middle index
#         if arr[mid] == target:
#             return mid
#
#         # If the target is less than the element at the middle index,
#         # update the right pointer to search the left half of the array
#         elif arr[mid] > target:
#             right = mid - 1
#
#         # If the target is greater than the element at the middle index,
#         # update the left pointer to search the right half of the array
#         else:
#             left = mid + 1
#
#     # If the target is not found in the array, return -1
#     return -1
#

# Example usage:
# arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
# target = 9
# print(binary_search(arr, target))  # Output: 4 (index of number 9 in the array)
