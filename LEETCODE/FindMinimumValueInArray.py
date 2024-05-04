# def FindMinimumValueInArray(arr):
#     num = len(arr)
#     for i in range(num):
#         for j in range(0, num - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
#
#
# arr = [32,34,3,23,4,5,5,7,55,3]
# FindMinimumValueInArray(arr)
# print(arr[0])

def find_minimum_value_in_array(arr):
    if not arr:
        return None  # Return None if the array is empty

    min_value = arr[0]  # Assume the first element is the minimum
    for num in arr:
        if num < min_value:
            min_value = num  # Update the minimum value if a smaller value is found
    return min_value

arr = [32, 34, 3, 23, 4, 5, 5, 7, 55, 3]
min_value = find_minimum_value_in_array(arr)
print("Minimum value in the array:", min_value)
