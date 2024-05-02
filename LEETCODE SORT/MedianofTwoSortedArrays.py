class Solution():
   def findMedianSortedArrays(self,nums1, nums2):
    # Merge the two sorted arrays
    merged = sorted(nums1 + nums2)
    total_length = len(merged)
    
    # Calculate median index/indices
    if total_length % 2 == 0:
        # Even number of elements
        median_index1 = total_length // 2
        median_index2 = median_index1 - 1
        median = (merged[median_index1] + merged[median_index2]) / 2.0 
    else:
        # Odd number of elements
        median_index = (total_length - 1) // 2
        median = merged[median_index]
    
    return median

# Example usage
nums1 = [1,2]
nums2 = [3,4]
sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))  # Output: 2.0
