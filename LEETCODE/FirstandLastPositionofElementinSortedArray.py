class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        l = []
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = len(nums) // 2
            if nums[mid] == target:
                l.append(mid)
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return l

        # if l:
        #     if len(l) == 1:
        #         return [l[0], l[0]]
        #     else:
        #         return [l[0], l[len(l) - 1]]
        # else:
        #     return [-1, -1]


s = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 5
print(s.searchRange(nums, target))
