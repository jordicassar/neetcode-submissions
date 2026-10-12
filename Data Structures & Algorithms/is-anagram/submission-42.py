class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for c in s:
            dict_s[c] = dict_s[c, 0] + 1
        
        for c in t:
            dict_t[c] = dict_s[c, 0] + 1
        
        return dict_s == dict_t