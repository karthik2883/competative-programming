def permute(nums):
    def backtrack(start):
        # Base case: If the start index is at the end of the list, we have found a permutation
        if start == len(nums):
            result.append(nums[:])  # Make a copy of the current permutation
            return
        
        # Explore all possible permutations by swapping elements
        for i in range(start, len(nums)):
            # Swap the elements at indices start and i
            nums[start], nums[i] = nums[i], nums[start]
            # Recursively generate permutations starting from the next index
            backtrack(start + 1)
            # Backtrack: Undo the swap to backtrack to the previous state
            nums[start], nums[i] = nums[i], nums[start]
    
    # Initialize an empty list to store the permutations
    result = []
    # Start backtracking from the beginning of the list
    backtrack(0)
    return result

# Example usage
nums = [1, 2, 3]
print(permute(nums))
