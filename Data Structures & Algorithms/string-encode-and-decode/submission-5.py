class Solution:

    def encode(self, strs: List[str]) -> str:
        # returned value must be in string form

        # initialize string variable
        result = []
        # iterate through loop
        for string in strs:
            result.append(str(len(string)))
            result.append("#")
            result.append(string)
        return "".join(result)

        
    def decode(self, s: str) -> List[str]:
        # returned value must be in string form

        # initialize list of strings
        result = []
        # 
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            result.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return result
