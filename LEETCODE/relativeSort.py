class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        res = []
        res2 = []
        for i in range(len(arr2)):
            el = arr2[i]
            for a in arr1:
                if a == el:
                    res.append(a)
        for value in arr1:
            if value not in res:
                res2.append(value)
        res2.sort()
        res.extend(res2)
        return res


s = Solution()
arr1 = [28, 6, 22, 8, 44, 17]
arr2 = [22, 28, 8, 6]
print(s.relativeSortArray(arr1, arr2))
