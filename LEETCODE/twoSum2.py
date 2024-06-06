class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


s = Solution()
numbers = [2,7,11,15]
print(s.twoSum(numbers,9))