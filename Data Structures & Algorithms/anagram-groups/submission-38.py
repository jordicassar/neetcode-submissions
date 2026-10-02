class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)

        for word in strs:
            # Characters within a-z
            count = [0] * 26
            for char in word:
                count[ord('a') - ord(char)] += 1  
            groups[tuple(count)].append(word)                                         
        return list(groups.values())            


