class Solution:
    def threeSum(self,nums):
        # Sort the input array
        nums.sort()

        # Initialize an empty list to store triplets
        triplets = []

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
                if total == 0:
                    # Found a triplet
                    triplets.append([nums[i], nums[left], nums[right]])
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

        return triplets


# Example usage:
sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
