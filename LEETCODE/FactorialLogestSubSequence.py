# def factorial_with_sequence(n, memo={}):
#     if n in memo:
#         return memo[n][0], memo[n][1]
#     if n <= 1:
#         return 1, [1]
#     sub_factorial, sub_sequence = factorial_with_sequence(n-1, memo)
#     memo[n] = n * sub_factorial, [n] + sub_sequence
#     return memo[n][0], memo[n][1]

# # Test
# result, sequence = factorial_with_sequence(5)
# print(f"Factorial: {result}, Sequence: {sequence}")  # Output: Factorial: 120, Sequence: [5, 4, 3, 2, 1]


# Tabulation example: Longest Increasing Subsequence (LIS) problem with sequence

# def lis_with_sequence(nums):
#     if not nums:
#         return 0, []
#     dp = [1] * len(nums)
#     sequences = [[num] for num in nums]
#     max_length = 1
#     max_index = 0
#     for i in range(1, len(nums)):
#         for j in range(i):
#             if nums[i] > nums[j] and dp[i] < dp[j] + 1:
#                 dp[i] = dp[j] + 1
#                 sequences[i] = sequences[j] + [nums[i]]
#                 if dp[i] > max_length:
#                     max_length = dp[i]
#                     max_index = i
#     return max_length, sequences[max_index]

# # Test
# length, sequence = lis_with_sequence([10, 22, 9, 33, 21, 50, 41, 60])
# print(f"Length of LIS: {length}, Sequence: {sequence}")  # Output: Length of LIS: 5, Sequence: [10, 22, 33, 50, 60]


def fibonacci_with_sequence(n, memo={}):
    if n in memo:
        return memo[n][0], memo[n][1]
    if n <= 1:
        return n, [0, 1][:n+1]  # Sequence for 0 or 1
    fib1, seq1 = fibonacci_with_sequence(n-1, memo)
    fib2, seq2 = fibonacci_with_sequence(n-2, memo)
    memo[n] = fib1 + fib2, seq1 + [fib1 + fib2]
    return memo[n][0], memo[n][1]

# Test
result, sequence = fibonacci_with_sequence(7)
print(f"The 7th Fibonacci number is: {result}")
print(f"The sequence up to the 7th Fibonacci number is: {sequence}")
