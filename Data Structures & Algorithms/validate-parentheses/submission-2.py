class Solution:
    def isValid(self, s: str) -> bool:
        close = "]})"
        closes = {
            '{': '}',
            '(': ')',
            '[': ']',
        }
        stack = []
        if s[0] in close:
            return False
        else:
            stack.append(s[0])
        index = 1
        while index < len(s):
            print(stack)
            
            if s[index] in closes: 
                stack.append(s[index])
            else:
                if not stack:
                    return False
                paren = stack.pop()
                if s[index] != closes[paren]:
                    print("oops")
                    return False
            index +=1
        if not stack: 
            return True
        return False

