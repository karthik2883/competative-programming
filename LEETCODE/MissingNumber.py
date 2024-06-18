# User function Template for python3
class Solution:

    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        arr.sort()
        l, r = 0, 1
        res = 0
        if arr[0] == 1 and len(arr) == 1:
            res = 2
            return res
        if arr[0] == 2:
            res = 1
            return res
        while r < n - 1:
            if arr[l] != arr[r] - 1:
                res = arr[r] - 1
                break
            r += 1
            l += 1

        return res


# {
# Driver Code Starts
# Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)

# } Driver Code Ends
