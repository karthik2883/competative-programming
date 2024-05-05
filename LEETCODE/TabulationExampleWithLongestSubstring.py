# def longest_substring_tab(s):
#     if not s:
#         return 0, ""

#     max_length = 0
#     start = 0
#     end = 0
#     max_substring = ""
#     char_index_map = {}

#     for i, char in enumerate(s):
#         if char in char_index_map and char_index_map[char] >= start:
#             start = char_index_map[char] + 1
#         char_index_map[char] = i
#         if i - start + 1 > max_length:
#             max_length = i - start + 1
#             end = i
#             max_substring = s[start:end + 1]

#     return max_length, max_substring

# # Test
# s = "abcabcbb"
# length, sequence = longest_substring_tab(s)
# print(f"Length of the longest substring: {length}, Sequence: {sequence}")  # Output: Length of the longest substring: 3, Sequence: abc

class Solution():
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0, ""

        max_length = 0
        start = 0
        end = 0
        max_substring = ""
        char_index_map = {}

        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            char_index_map[char] = i
            if i - start + 1 > max_length:
                max_length = i - start + 1
                end = i
                max_substring = s[start:end + 1]

        return max_length, max_substring


string_check = "abcabcbb"
s = Solution()
#  The answer is "abc", with the length of 3.
length, sequence = s.lengthOfLongestSubstring(string_check)
print(f"The answer is {sequence}, with the length of {length}.")