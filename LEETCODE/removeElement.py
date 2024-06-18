class Solution(object):
    def removeElement(self, nums, val):
        v, nv = 0, 0
        n = len(nums)
        res = []
        while v < n:
            if nums[v] != val:
                nums[v], nums[nv] = nums[nv], nums[v]
                nv += 1
                v += 1
            else:
                v += 1
        return nv


nums = [0,1,2,2,3,0,4,2]
val = 2
s = Solution()
print(s.removeElement(nums, val))
