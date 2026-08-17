class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            "(": ")", 
            "{": "}",
            "[": "]"
        }

        stack = []

        

        for character in s: 
            if character in parens: 
                # Start of the paren so append to the stack. 
                stack.append(character)
            
            elif not stack:
                return False
            elif parens[stack[-1]] == character: 
                stack.pop()
            else: 
                return False
        if not stack: 
            return True
        return False