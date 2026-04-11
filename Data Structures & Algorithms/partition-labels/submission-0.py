from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # sounds kind of easy.

        freqs = Counter(s)

        count = 0
        need = {}
        result = []
        for i in range(len(s)):            
            if need.get(s[i]) == None: #this is the first time we encounter. 
                need[s[i]] = freqs[s[i]] - 1 # because we already see it once
            else:
                need[s[i]] -=1
            count += 1 
            if need[s[i]] == 0: 
                del need[s[i]]
            if not need: 
                result.append(count)
                count = 0
        return result
            

        