class Solution:
    def findMaxK(self, nums):

        s = len(nums)
        min_value = -1
        j = 0

        while j < s:
            # print(j)
            if min_value < nums[j] and -nums[j] in nums  :
                min_value = nums[j]
            
            j += 1


        return min_value


nums = [-10,8,6,7,-2,-3]
s = Solution()
print(s.findMaxK(nums))
