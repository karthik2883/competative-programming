def group_anagrams(words):
    anagrams_map = {}
    
    # Iterate through each word in the list
    for word in words:
        # Sort the characters of the word to create a unique key for anagrams
        sorted_word = ''.join(sorted(word))
        
        # Check if the sorted word exists in the dictionary
        if sorted_word in anagrams_map:
            # If exists, append the original word to the list of anagrams
            anagrams_map[sorted_word].append(word)
        else:
            # If doesn't exist, create a new entry in the dictionary
            anagrams_map[sorted_word] = [word]
    
    # Convert the values (lists of anagrams) of the dictionary to a list
    return list(anagrams_map.values())

# Example usage:
words = ["listen", "silent", "enlist", "heart", "earth", "hello", "world"]
print(group_anagrams(words))
