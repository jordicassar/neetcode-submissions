class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check for of both strings
        if len(s) != len(t):
            return False
        
        # Initialize dict for both strings
        dict_s = {}
        dict_t = {}

        # Iterate through strings s and t. char is our key and 0 is our value
        # when initializing, (+ 1) is the incremental once a char is already in 
        # the dictionary.
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
        
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
    
        # Return if both dictionaries 
        # are equal to each other   
        return dict_s == dict_t