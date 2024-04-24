# from typing import List
#
#
# def sort_scores(nums: List[int]) -> List[int]:
#     max_val = max(nums)
#     count = [0] * (max_val + 1)
#     for num in nums:
#         count[num] += 1
#     output = []
#     for i in range(len(count)):
#         # print([i] * count[i])
#         output.extend([i] * count[i])
#     return output
#
#
# nums = [23, 23, 1, 12,77, 4, 5, 32]
#
# print(sort_scores(nums))


"""
Initialize Variables:

max_val = max(arr): Determine the maximum value in the input array arr.
count = [0] * (max_val + 1): Create a counting array count with a length of max_val + 1 initialized to all zeros. Each index represents a value from 0 to max_val, and the value at each index will represent the count of occurrences of that value in the input array.
Counting Occurrences:

for num in arr:: Iterate through each element num in the input array arr.
count[num] += 1: Increment the count of occurrences for the value num in the count array.
Generate Output:

output = []: Initialize an empty list output to store the sorted elements.
for i in range(len(count)):: Iterate through each index i in the count array.
output.extend([i] * count[i]): Append i to the output list count[i] times. This step effectively reconstructs the sorted array by appending each value i the number of times it appeared in the original input array arr.
Return Output:

return output: Return the sorted output list.
Overall, counting sort works by first counting the occurrences of each element in the input array, then reconstructing the sorted array based on the counts of each element. It is efficient for sorting integers with a limited range and has a linear time complexity of O(n + k), where n is the number of elements in the input array and k is the range of input values.
"""


def CountingSort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)
    for num in arr:
        count[num] += 1
    output = []
    for i in range(len(count)):
        output.extend([i] * count[i])
    return output


a = [13, 5, 5, 6, 4, 3, 2]

print(CountingSort(a))
