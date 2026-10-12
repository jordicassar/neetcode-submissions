class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        map = defaultdict(list)

        # Traverse through the strs list
        # w represents word
        for word in strs:
            # Initialize count list
            count = [0] * 26
            
            # c represents characters in w 
            for char in word:
                count[ord('c') - ord('a')] += 1
            map[tuple(count)].append(word)

        return list(map.values())
