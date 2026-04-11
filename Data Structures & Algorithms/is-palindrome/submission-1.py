class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [ch.lower() for ch in s if ch.isalnum()]

        start  = 0
        end = len(filtered) - 1

        for i in filtered: 
            if i != filtered[end]:
                return False
            end -= 1
        return True
