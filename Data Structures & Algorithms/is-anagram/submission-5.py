class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Dictionary Initialization
        dict_s = {}
        dict_t = {}

        # Passing through string s
        for c in s:
            dict_s[c] = dict_s.get(c, 0) + 1
        
        # Passing through string t
        for c in t:
            dict_t[c] = dict_t.get(c, 0) + 1
        
        # Return true if both strings contain the same characters
        return dict_t == dict_s

            