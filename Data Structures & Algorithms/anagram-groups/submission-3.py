class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can encode each of these into 26 length strings. Check if they are equal, and then group them together. 

        hasher = {}
        for word in strs: 
            encoder = [0] * 26
            for character in word: 
                encoder[ord(character) - ord('a')] += 1
            encoded = tuple(encoder)
            hasher[encoded] = hasher.get(encoded, [])
            hasher[encoded].append(word)
        result = []

        for key in hasher: 
            result.append(hasher[key])
        return result
