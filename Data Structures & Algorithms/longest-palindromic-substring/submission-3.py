class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for i in range(len(s))]

        start, maxlen = 0, 1

        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s) -1 ):
            if s[i] == s[i +1]:
                dp[i][i+1] = True
                start = i
                maxlen = 2

        for i in range(3, len( s) + 1):
            for k in range(len(s) - i + 1):
                j = i +k -1
                if s[k] == s[j] and dp[k + 1][j - 1]:
                    dp[k][j] = True
                    start = k 
                    if i > maxlen: 
                        start = k
                        maxlen = i
        return s[start: start + maxlen]
