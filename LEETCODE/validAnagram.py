class Solution(object):
    def isAnagram(self, s, t):
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False
        if len(s) != len(t):
            return False
        conterS, conterT = {}, {}
        for i in range(len(s)):
            conterS[s[i]] = 1 + conterS.get(s[i], 0)
            conterT[t[i]] = 1 + conterT.get(t[i], 0)

        for c in conterS:
            if conterS[c] != conterT.get(c, 0):
                return False
        return True


sol = Solution()
s = "rat"
t = "car"
print(sol.isAnagram(s,t))