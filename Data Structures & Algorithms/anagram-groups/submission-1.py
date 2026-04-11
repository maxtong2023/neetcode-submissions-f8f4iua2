class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        alphabet = [0] * 26
        freqs = {}
        index = 0
        results = []

        for i in strs:
            for k in i:
                index = ord(k) - 97
                alphabet[index] = alphabet[index] +1
            if(freqs.get(tuple(alphabet)) == None):
                freqs[tuple(alphabet)] = [i]
            else:
                freqs[tuple(alphabet)].append(i)
            alphabet = [0] * 26
        return list(freqs.values())
