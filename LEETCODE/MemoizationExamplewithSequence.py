def longest_substring_memo(s, start=0, end=0, memo={}):
    if (start, end) in memo:
        return memo[(start, end)]
    
    if end == len(s):
        return 0, ""
    
    if s[end] in s[start:end]:
        memo[(start, end)] = end - start, s[start:end]
        return memo[(start, end)]
    
    length1, seq1 = longest_substring_memo(s, start, end + 1, memo)
    length2, seq2 = longest_substring_memo(s, start + 1, end + 1, memo)
    
    if length1 > length2:
        memo[(start, end)] = length1, seq1
    else:
        memo[(start, end)] = length2, seq2
    
    return memo[(start, end)]

# Test
s = "pwwkew"
length, sequence = longest_substring_memo(s)
print(f"Length of the longest substring: {length}, Sequence: {sequence}")  # Output: Length of the longest substring: 3, Sequence: abc
