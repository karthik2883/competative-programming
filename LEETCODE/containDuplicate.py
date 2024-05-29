class Solution(object):
    def containsDuplicate(self, nums):
        if not nums:
            return 0
        container = set()
        for num in nums:
            if num in container:
                return True
            else:
                container.add(num)
        return False


nums = [0, 4, 5, 0, 3, 6]
s = Solution()
print(s.containsDuplicate(nums))
