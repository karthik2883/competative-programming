class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevDiff = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevDiff:
                return [prevDiff[diff], i]
            prevDiff[n] = i
        return []

sol = Solution()
s = [2,7,11,15]
t = 17
print(sol.twoSum(s,t))