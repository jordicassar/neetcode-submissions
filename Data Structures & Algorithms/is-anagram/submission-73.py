class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initialize dictionaries
        dict_s = {}
        dict_t = {}

        for c in s:
            dict_s[c] = dict_s.get(c, 0) + 1
        
        for c in t:
            dict_t[c] = dict_t.get(c, 0) + 1
        
        return dict_t == dict_s