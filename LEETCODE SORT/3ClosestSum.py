class Solution:
    def threeSumClosest(self,nums,target):
        # Sort the input array
        nums.sort()

        # Initialize an empty list to store triplets
        sumOfall = 0

        # Iterate over each element nums[i]
        for i in range(len(nums) - 2):
            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize left and right pointers
            left, right = i + 1, len(nums) - 1

            # Two pointer traversal
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total >= target:
                    # Found a triplet
                    sumOfall = total
                    # Skip duplicate elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Move pointers to find other pairs
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return sumOfall


# Example usage:
sol = Solution()
nums = [1,1,-1]
print(sol.threeSumClosest(nums,2))  #
"""Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

"""
