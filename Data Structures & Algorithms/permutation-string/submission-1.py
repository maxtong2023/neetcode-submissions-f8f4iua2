class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # a permutation is when you have the exact same number of characters 
        # and the exact same frequency 
        

        freqs = [0] * 26
        match = [0] * 26
        if len(s1) > len(s2): 
            return False

        for i in s1: 
            freqs[ord(i) - 97] += 1

        left = 0 
        right = len(s1) - 1

        for ch in s2[:len(s1)]:
            match[ord(ch) - 97] += 1

        for i in range(len(s1), len(s2)):
            if match == freqs:
                return True
            match[ord(s2[i - len(s1)]) - 97] -= 1  # char leaving
            match[ord(s2[i]) - 97] += 1      # char entering

        return match == freqs

