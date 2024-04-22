# def two_sum(nums, target):
#     nums.sort()
#     left = 0
#     right = len(nums) - 1
#
#     while left < right:
#         current_sum = nums[left] + nums[right]
#
#         if current_sum == target:
#             return [nums[left], nums[right]]
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
#     return None

def two_sum(nums, target):
    nums_indices = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in nums_indices:
            return [nums_indices[compliment], i]
        nums_indices[num] = i
    return []


# Example usage:
nums = [-2, 7, -11, -3, 4, -22, 32, 15]
target = 1
result = two_sum(nums, target)
print("Two numbers that sum up to", target, "are:", result)
