def letter_combinations(digits):
    # Define the mapping of digits to letters
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    # Define a recursive function to generate letter combinations
    def backtrack(index, path):
        # Base case: If the current path is of the same length as the input digits, add it to the result
        if len(path) == len(digits):
            result.append(path)
            return
        
        # Get the letters corresponding to the current digit
        letters = mapping[digits[index]]
        
        # Iterate over each letter and recursively generate combinations
        for letter in letters:
            backtrack(index + 1, path + letter)
    
    # Initialize an empty list to store the result
    result = []
    
    # Check if the input digits are not empty, then start backtracking
    if digits:
        backtrack(0, '')
    
    return result

# Example usage
digits = "23"
print(letter_combinations(digits))
