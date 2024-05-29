class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        key = ""
        res = []
        for word in words:
            new_key = ''.join(sorted(word))
            if new_key != key:
                key = new_key
                res.append(word)

        return res


s = Solution()
arr = ["abba", "baba", "bbaa", "cd", "cd"]
print(s.removeAnagrams(arr))


