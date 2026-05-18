class Solution:
    def numDecodings(self, s: str) -> int:
        # given two digits, it can be seperated into at least 0 
        # differnt encodings, at most 2. The character with 
        # digit 1, the character with digit 2, and the character 
        # with both digits. 

        # ex 12 can be "ab" or "j". 

        #iterate through the string array once. At any given index
        # of the string, define opt to be the max amount of decodings
        # you can make.

        # 12345

        # ABCDE - uses 1 for each index
        # AWDE - 1, 23, 4, 5,
        # LCDE - 12, 3, 4, 5

        # check the current index, then check s[i-1: i]?

        # 1 can only make 1 decoding
        # 12, 12 can be a decoding, so can 1 2, now we have 2? 
        # 123, 3 is a decoding, so is 23... now we have 3?
        # 1234, 4 is a decoding, but 34 is not, do not increment
        # 12345, 5 is a decoding, but 45 is not, do not increment 

        # 12045

        # 1 can make one decoding 
        # 12, 2 can make one decoding, 12 can make another, increment 1.
        # 0 is not a decoding, 20 is, do not change. 
        # 4 is a decoding, 04, is not. 
        # 5 is a decoding, 45 is not. 

        # total is 1 decoding?

        #fact check: 
        # ATDE. yes. 
        

        dp = [0] * (len(s) + 1)

        dp[0] = 1
        if s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, len(s)+ 1):
            if s[i - 1] != "0":
                dp[i] += dp[i-1]
            if int(s[i-2: i]) >9 and int(s[i-2: i]) < 27: 
                dp[i] += dp[i - 2]
        return dp[len(s)]




        