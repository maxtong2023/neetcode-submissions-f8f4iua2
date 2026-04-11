class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        letters = {}

        if(len(s) != len(t)):
            return False


        for k in t: 
            if(letters.get(k) == None):
                letters[k] = 1
            else:
                letters[k] = letters[k] + 1

        for i in s: 
            if(letters.get(i) == None):
                return False
            elif(letters[i] == 0):
                return False
            else:
                letters[i] = letters[i] -1
        return True






        