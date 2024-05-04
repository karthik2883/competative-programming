# Tabulation example: Longest Increasing Subsequence (LIS) problem

def lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Test
print(lis([10, 22, 9, 33, 21, 50, 41, 60]))  # Output: 5
