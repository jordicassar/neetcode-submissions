class Solution:
     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Import defaultdict from collections
        from collections import defaultdict

        # Map initialization
        map = defaultdict(list)

        # Loop through every word in strs
        for word in strs:
            # Initialize count list
            count = [0] * 26
            # Loop through each character in w
            for char in word:
                count[ord(char) - ord('a')] += 1
            map[tuple(count)].append(word)

        return list(map.values())
