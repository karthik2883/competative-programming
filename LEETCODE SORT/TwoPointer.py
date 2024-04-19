def two_sum(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


# Example usage:
nums = [-1, 2, 1, -4]
target = 1
result = two_sum(nums, target)
print("Two numbers that sum up to", target, "are:", result)
