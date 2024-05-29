from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, arr):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for a in arr:
            count = [0] * 26
            for s in a:
                count[ord(s) - ord("a")] += 1
            res[tuple(count)].append(a)

        return res.values()

s = Solution()
arr = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(arr))
