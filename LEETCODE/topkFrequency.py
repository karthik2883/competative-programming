class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            frequency[c].append(n)
        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res


nums = [1, 1, 3, 3, 1, 2, 2, 3]
k = 3
s = Solution()

print(s.topKFrequent(nums, k))
