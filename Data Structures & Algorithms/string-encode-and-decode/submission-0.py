class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for i in strs: 
            result.append(str(len(i)) + "#")
            result.append(i)
        return "".join(result)


    def decode(self, s: str) -> List[str]:
        index = 0
        counter = 0
        start = 0
        result = []
        #finds the length of the string.
        while index < len(s):
            while s[index] != "#":
                counter = int(s[start: index+1])
                index += 1
            result.append(s[index + 1: index +counter + 1])
            index = index + counter + 1
            start = index
        return result
