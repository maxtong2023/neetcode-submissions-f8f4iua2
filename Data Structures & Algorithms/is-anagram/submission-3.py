class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        if len(s) != len(t):
            return False

        for i in s: 
            freqs[i] = freqs.get(i, 0 ) +1 
        for i in t: 
            if freqs.get(i) == None: 
                return False
            else: 
                freqs[i] -= 1
                if freqs[i] == 0:
                    freqs.pop(i)
        if not freqs: 
            return True