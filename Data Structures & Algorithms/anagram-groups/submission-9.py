class Solution:
     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        map = defaultdict(list)

        for word in strs:

            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1
            map[tuple(count)].append(word)
        
        return list(map.values())
