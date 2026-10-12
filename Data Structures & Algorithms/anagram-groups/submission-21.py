class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count += (ord(char) - ord('a'))
            groups[char].append(word)
        return groups.list()