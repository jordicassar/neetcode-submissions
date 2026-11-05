class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)

        # iterate over the strs list
        for word in strs:
            # we need to keep track of characters
            # a-z
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())