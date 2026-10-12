class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        for c in s:
            dict_s = dict_s.get(0, c) + 1
        for c in t:
            dict_t = dict_t.get(0, c) + 1

        return dict_s == dict_t