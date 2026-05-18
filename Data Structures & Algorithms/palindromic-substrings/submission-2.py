class Solution:
    def countSubstrings(self, s: str) -> int:
        # do the same thing that you just did but keep a counter of the 
        # palindromes? 

        count = 0 

        dp = [[False] * len(s) for i in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
            count += 1

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1
        for i in range(3, len(s) + 1):
            for k in range(len(s) - i + 1):
                j = i + k - 1

                if s[k] == s[j] and dp[k+1][j-1]:
                    count += 1
                    dp[k][j] = True

        return count
