from typing import List


def find_combinations(s: str) -> List[str]:
    # Define a helper function for backtracking
    def backtrack(index: int, path: str):
        # Base case: If the length of the current combination is equal to the length of the input string
        if len(path) == len(s):
            result.append(path)  # Add the current combination to the result
            return
        
        # If the current character is '0', replace it with 'A'; if it's '1', replace it with 'B'
        if s[index] == '0':
            backtrack(index + 1, path + 'A')  # Try replacing with 'A'
            backtrack(index + 1, path + 'B')  # Try replacing with 'B'
        else:
            backtrack(index + 1, path + 'B')  # Try replacing with 'B'
            backtrack(index + 1, path + 'A')  # Try replacing with 'A'

    # Initialize an empty list to store the result
    result = []
    # Start backtracking from the beginning of the string
    backtrack(0, '')
    return result

# Example usage
s = "101"
print(find_combinations(s))
